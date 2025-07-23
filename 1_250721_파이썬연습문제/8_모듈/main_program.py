'''
문제 8-1 (중/하)
설명: 수학 연산을 위한 모듈을 만들고 이를 사용하는 메인 프로그램을 작성하세요.
 파일명: main_program.py, math_operations.py
 출력결과:
원의 넓이: 78.54
직사각형 넓이: 50
팩토리얼 5! = 120
최대공약수(48, 18) = 6
'''

import math_operations as mo

print(f"원의 넓이: {mo.circle(5)}", )
print(f"직사각형 넓이: {mo.rect(10, 5)}" )
print(f"팩토리얼 5! = {mo.fact(5)}")
print(f"최대공약수(48, 18) = {mo.gcd(48, 18)}")