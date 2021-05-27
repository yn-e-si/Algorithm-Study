from typing import *

# 풀이 1
def threeSum(nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    answer = []
    for i in range(len(nums)):
        left, right = i+1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if  three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                answer.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
    answer = set(answer)

    return [list(i) for i in answer]

# 풀이 2 - 최적화
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] ==nums[i - 1]:
            continue
        # 간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if  three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                # sum = 0 인 경우이므로 정답 및 스킵 처리
                results.append((nums[i], nums[left], nums[right]))
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return results