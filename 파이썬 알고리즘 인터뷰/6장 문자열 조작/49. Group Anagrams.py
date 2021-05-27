from typing import *
import collections
# 풀이 1
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    count = []
    check = [[s,0] for s in strs]
    strs_list = [ [] for _ in range(len(strs))]
    for s in strs:
        count.append([Counter(s)])
    for idx1 in range(len(strs)):
        for idx2 in range(idx1+1,len(strs)):
            if count[idx1] == count[idx2] and  check[idx2][1] == 0:
                if check[idx1] == 0:
                    strs_list[idx1].append(strs[idx1])
                    strs_list[idx1].append(strs[idx2])
                    check[idx1][1] = 1
                    check[idx2][1] = 1
                else:
                    strs_list[idx1].append(strs[idx2])
                    check[idx2][1] = 1

    for idx, value in enumerate(strs):
        if check[idx][1] == 0:
            strs_list[idx].append(value)

    return [ strs for strs in strs_list if strs]


# 풀이 2
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())