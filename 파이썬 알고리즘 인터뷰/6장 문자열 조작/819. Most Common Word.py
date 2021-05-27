from typing import *
import re, collections
# 풀이 1
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
        
    for para in paragraph:
        if (not para.isalpha()) and para != ' ' :
            paragraph = paragraph.replace(para, ' ')
    for para in paragraph.split():
        if para in banned:
            paragraph = paragraph.replace(para, ' ', 1)

    return Counter(paragraph.split()).most_common(1)[0][0]


# 풀이 2
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    
    return counts.most_common(1)[0][0]