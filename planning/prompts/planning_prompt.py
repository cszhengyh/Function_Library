planning_prompt = r"""
You are a champion of the International Collegiate Programming Contest and the International Olympiad in Informatics, and you are a senior Python engineer. You will be provided with a competitive programming problem and multiple python functions. Your task is to write a python solve function `solve()` to solve this competitive programming problem that can call multiple functions provided. Deliver your response in this format: [solve_function: ......, function_list: ......]. The solve_function is the solve function you write, and function_list is the function name of the functions that the solve function calls. The solve function can only call the provided functions. 
For example, the problem is "A", the functions are "def B():\n    return 1, def C()\n    return 2, def D()\n    return 3, def E()\n    return 4, def F()\n    return 6". Because the solve function is
```
def solve():
    if B():
        return C()
    else:
        return D()
```
, your response should be [solve_function: def solve():\n    if B():\n        return C()\n    else:\n        return D(), function_list: B, C, D.
"""