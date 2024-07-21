# python /share/project/zhengyuhui/code_benchmark/implementation/generate_sample.py > /share/project/zhengyuhui/code_benchmark/human-eval/samples.jsonl
FUNC_POOL_PATH = ""

import jsonlines
from chat_with_gpt import chat_with_gpt
from prompts.implementation_prompt import implementation_prompt

def generate_model_response(function_desp):
    def call_llm(query):
        return chat_with_gpt(query)

    query = implementation_prompt + f"Now, the python function description is \"{function_desp}\". Please respond following the above requirements and examples."
    response = call_llm(query)
    return response

sample_json = []

with jsonlines.open(FUNC_POOL_PATH, 'r') as func_pool_file:
    idx = 0
    for line in func_pool_file:
        function = line['function']
        prompt, canonical_solution = function.split(r"\n    \"\"\"\n")
        prompt += r"\n    \"\"\"\n"

        while True:
            response = generate_model_response(prompt)
            if re.findall(r'\[function: \s*(.*?)\]', response)[0]:
                completion = re.findall(r'\[function: \s*(.*?)\]', response)[0]
                break
            else:
                continue

        sample_json.append('{' + f"\"task_id\": \"CPEval/{idx}\", \"completion\": \"{completion}\"" + '}')

        idx += 1

for item in sample_json:
    print(item)