# python /share/project/zhengyuhui/code_benchmark/planning/generate_planning_evaluation_data.py > /share/project/zhengyuhui/code_benchmark/planning/planning_data/planning_data.jsonl
FUNC_POOL_PATH = ""
PROBLEM_TO_FUNCLIST_PATH = ""
PLANNING_TEST_DATA_OUT_PATH = "/share/project/zhengyuhui/code_benchmark/planning/planning_data/planning_test_data.jsonl"

import re
import random
import jsonlines
from chat_with_gpt import chat_with_gpt
from collections import default_dict
from prompts.planning_prompt import planning_prompt

func_pool = []
problem_to_funclist = default_dict(lambda: [])

# read func_pool
with jsonlines.open(FUNC_POOL_PATH, 'r') as func_pool_file:
    for line in func_pool_file:
        func_pool.append(line['function'])

# read problem_to_funclist
with jsonlines.open(PROBLEM_TO_FUNCLIST_PATH, 'r') as problem_to_funclist_file:
    for line in problem_to_funclist_file:
        problem_to_funclist[line['problem']] = line['func_list']

def sampling_neg_funcs(pool, cnt):
    res = []
    sgt = range(0, len(pool))
    sample_ids = random.sample(sgt, cnt)
    for sample_idx in sample_ids:
        res.append(pool[sample_idx])
    return res

for problem, funclist in problem_to_funclist.items():
    temp_pool = func_pool
    for func in funclist:
        func_pool.remove(func)
    sample_cnt =  # ?
    neg_funcs = sampling_neg_funcs(func_pool, sample_cnt)
    func_pool = temp_pool
    planning_data = "{"+f"problem: {problem}, func_list: {neg_funcs+funclist}"+"}\n"
    print(planning_data)
