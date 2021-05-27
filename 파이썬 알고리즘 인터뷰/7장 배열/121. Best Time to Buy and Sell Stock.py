from typing import *
import sys
# 풀이 1
def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    min_num = sys.maxsize

    for price in prices:
        min_num = min(min_num, price)
        answer = max(answer, price - min_num)
    return answer