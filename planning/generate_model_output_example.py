PLANNING_DATA_PATH = "/share/project/zhengyuhui/code_benchmark/planning/planning_data/planning_data.jsonl"

import re
import jsonlines
from chat_with_gpt import chat_with_gpt
from prompts import planning_prompt

def generate_model_response(problem, func_list):
    # user code
    def call_llm(query):
        '''
        call your llm to respond query
        '''
        return chat_with_gpt(query)

    query = planning_prompt + f"Now, the problem is \"{problem}\", the functions are \"{', '.join(func_list)}\". Please respond following the above requirements and examples."
    response = call_llm(query)
    return response

with jsonlines.open(PLANNING_DATA_PATH, 'r') as PLANNING_DATA_FILE:
    for planning_data in PLANNING_DATA_FILE:
        while True:
            solution = ""
            response = generate_model_response(planning_data['problem'], planning_data['func_list']) 
            if re.findall(r'\[solve_function: \s*(.*?),\s*function_list: \s*(.*?)\]', response):
                match = re.findall(r'\[solve_function: \s*(.*?),\s*function_list: \s*(.*?)\]', response)
                func_list = list(set(match[1].split(", ")))
                for func_name in func_list:
                    flag = 0
                    for func in planning_data['func_list']:
                        temp = re.findall(r'def \s*(.*?)\(', func)[0]
                        if func_name == temp:
                            solution += func+'\n\n'
                            flag = 1
                            break
                    if flag == 0:
                        break
                if flag == 0:
                    print(f"{func_name} is not exist!")
                    continue
                solution += match[0]+"\n\nsolve()"
                break
            else:
                continue

        print(planning_data['problem'])
        print("\n```")
        print(solution)
        print("```")
        print("\n===================================================\n")