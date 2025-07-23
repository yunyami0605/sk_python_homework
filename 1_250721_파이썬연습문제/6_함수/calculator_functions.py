'''
문제 6-1 (하)
설명: 두 수를 받아서 사칙연산을 수행하는 함수들을 작성하는 프로그램을 만드세요.
 파일명: calculator_functions.py
 출력결과:
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0

'''

def tmp(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {(a / b):.1f}")

tmp(10, 5)