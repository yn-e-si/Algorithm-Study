from typing import *

# 풀이 1
def twoSum(nums: List[int], target: int) -> List[int]:
    for n1 in range(len(nums)):
        for n2 in range(n1+1,len(nums)):
            if nums[n1] + nums[n2] == target:
                return [n1,n2]

# 풀이  2 - in 을 이용한 탐색
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target -n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

# 풀이 3 - 첫 번째 수를 뺀 결과 키 조회
def twoSum(nums: List[int], target: int) -> List[int]:
    # 키와 값을 바꿔서 딕셔너리로 저장
    nums_map = { num: i for i, num in enumerate(nums)}

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# 풀이 4 - 조회 구조 개선
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 풀이 5 - 투 포인터 이용
def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]