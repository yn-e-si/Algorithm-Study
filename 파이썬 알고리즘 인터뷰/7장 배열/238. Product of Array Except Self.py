from typing import *

# 풀이 1
def productExceptSelf(nums: List[int]) -> List[int]:
    multiply_num = 1
    answer = []

    for i in range(0,len(nums)):
        answer.append(multiply_num)
        multiply_num *= nums[i]
    
    multiply_num = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= multiply_num
        multiply_num *= nums[i]

    return answer