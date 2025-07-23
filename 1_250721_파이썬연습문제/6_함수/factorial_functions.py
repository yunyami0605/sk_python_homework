'''
문제 6-2 (중/하)
설명: 팩토리얼을 계산하는 재귀함수와 반복문을 사용한 함수를 각각 작성하세요.
 파일명: factorial_functions.py
 출력결과:
5! (재귀) = 120
5! (반복) = 120
7! (재귀) = 5040
7! (반복) = 5040

'''

def tmp(n):
    if n == 1: 
        return 1
    
    return n * tmp(n - 1)

def tmp2(n):
    sum = 1
    while n != 1:
        sum *= n
        n -= 1

    return sum

print(f"5! (재귀) = {tmp(5)}")
print(f"5! (반복) = {tmp2(5)}")
print(f"7! (재귀) = {tmp(7)}")
print(f"7! (반복) = {tmp2(7)}")
