from typing import *

# 풀이 1
def isPalindrome(s: str) -> bool:
    sentence = ""
    for i in s:
        if i.isalnum():
            sentence += i.lower()
                
    for idx, value in enumerate(sentence):
        if value == sentence[-idx -1]:
            pass
        else:
            return False
    else:
        return True

# 풀이 2
def isPalindrome(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

# 풀이 3
def isPalindrome(s: str) -> bool:
    
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 풀이 4
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱