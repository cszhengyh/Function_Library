# python /share/project/zhengyuhui/code_benchmark/implementation/generate_human_eval.py > /share/project/zhengyuhui/code_benchmark/human-eval/data/HumanEval.jsonl && gzip -k /share/project/zhengyuhui/code_benchmark/human-eval/data/HumanEval.jsonl
FUNC_POOL_PATH = ""

import jsonlines

human_eval_jsonl = []

with jsonlines.open(FUNC_POOL_PATH, 'r') as func_pool_file:
    idx = 0
    for line in func_pool_file:
        function = line['function']
        prompt, canonical_solution = function.split(r"\n    \"\"\"\n")
        prompt += r"\n    \"\"\"\n"
        entry_point = re.findall(r'def \s*(.*?)\(', prompt)[0]

        test_case_list = line['test']

        '''
        \n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate(3.5) == 0.5\n    assert abs(candidate(1.33) - 0.33) < 1e-6\n    assert abs(candidate(123.456) - 0.456) < 1e-6\n
        '''
        test = r"\n\nMETADATA = {\n    'author': 'Yuhui Zheng',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n"
        for test_case in test_case_list:
            input = test_case['input']
            std = test_case['std']
            test += rf"    assert candidate({input}) == {std}\n"

        human_eval_jsonl.append('{' + f"\"task_id\": \"CPEval/{idx}\", \"prompt\": \"{prompt}\", \"entry_point\": \"{entry_point}\", \"canonical_solution\": \"{canonical_solution}\", \"test\": \"{test}\"" + '}')

        idx += 1

for item in human_eval_jsonl:
    print(item)