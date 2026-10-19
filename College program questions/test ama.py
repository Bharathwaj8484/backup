#!/bin/python3

import os

#
# Complete the 'getOutlierValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getOutlierValue(arr):
    set_nums = set(arr)
    res = -1
    sum_nums = sum(arr)
    for i in range(len(arr)):
        ans = sum_nums - arr[i]
        if ans % 2 == 0:
            if ans // 2 in set_nums:
                res = max(res, arr[i])
    return res

if __name__ == '__main__':
    # Sample Test Case Inputs
    test_cases = [
        {"input": [4, 1, 3, 16, 2, 10], "expected": 16},
        {"input": [2, 2, 4, 2], "expected": 2},
        {"input": [4, 1, 2, 1, 10, 3], "expected": 1},
        {"input": [5, 8, 2, 3, 18, 8], "expected": 18},
        {"input": [1000000000, 1, 999999999, 1000000000], "expected": 1000000000},
    ]

    for idx, test in enumerate(test_cases):
        arr = test["input"]
        expected = test["expected"]
        result = getOutlierValue(arr)
        print(f"Test Case {idx + 1}: {'Passed' if result == expected else f'Failed (Expected {expected}, Got {result})'}")
