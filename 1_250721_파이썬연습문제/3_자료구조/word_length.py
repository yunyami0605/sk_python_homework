'''
문제 3-7 (중/하)
설명: 단어들이 담긴 리스트에서 가장 긴 단어와 가장 짧은 단어를 찾는 프로그램을 작성하세요.
 파일명: word_length.py
 출력결과:
단어 목록: ['cat', 'elephant', 'dog', 'butterfly', 'ant']
가장 긴 단어: butterfly (9글자)
가장 짧은 단어: cat (3글자)
'''

import math

word = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

maxLen = 0
minLen = math.inf
maxStr = ""
minStr = ""

for item in word:
    
    tmp = len(item)

    if tmp > maxLen:
        maxLen = tmp
        maxStr = item
    
    if tmp < minLen:
        minLen = tmp
        minStr = item

print(f"단어 목록: {word}")
print(f"가장 긴 단어: {maxStr} ({maxLen}글자)")
print(f"가장 짧은 단어: {minStr} ({minLen}글자)")
