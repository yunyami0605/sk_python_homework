'''
문제 5-10 (중/하)
설명: 삼항 연산자와 조건부 표현식을 사용하는 예제를 작성하세요.
 파일명: conditional_expression.py
 출력결과:
점수: 85, 결과: 합격
나이: 17, 상태: 미성년자
숫자들의 최대값: 42
양수들: [5, 12, 8, 23]
'''

score = 85
r1 = "합격" if score >= 80 else "불합격"

age = 17
r2 = "성인" if age >= 18 else "미성년자"

n = [3, 12, 42, -10]
r3 = max(n) if n else 0

n2 = [5, 12, 8, -10, 23, -20]
n4 = [n3 for n3 in n2 if n3 > 0]

print(f"점수: {score}, 결과: {r1}")
print(f"나이: {age}, 상태: {r2}")
print(f"숫자들의 최대값: {r3}")
print(f"양수들: {n4}")
