from typing import *

# 풀이 1
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    answer = 0
    for i in range(0,len(nums)-1,2):
        answer += min(nums[i],nums[i+1])
    return answer

# 풀이 2 - 파이썬다운 방식
def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])