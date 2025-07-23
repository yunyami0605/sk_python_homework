'''
설명: 사용자가 입력한 숫자가 소수인지 판별하는 프로그램을 작성하세요.
 파일명: prime_checker.py
 출력결과:
숫자를 입력하세요: 17
17은 소수입니다.

'''

n = int(input("숫자를 입력하세요: "))

tmp = n
count = 0
while tmp != 0:
    if n % tmp == 0:
        count += 1
    tmp -= 1

if count == 2:
    print(f"{n}은 소수입니다.")
