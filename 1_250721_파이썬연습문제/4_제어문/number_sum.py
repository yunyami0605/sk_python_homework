'''
설명: 숫자를 계속 입력받아서 0을 입력할 때까지 합계를 구하는 프로그램을 작성하세요.
 파일명: number_sum.py
 출력결과:
숫자를 입력하세요 (0을 입력하면 종료): 10
숫자를 입력하세요 (0을 입력하면 종료): 20
숫자를 입력하세요 (0을 입력하면 종료): 15
숫자를 입력하세요 (0을 입력하면 종료): 0
입력된 숫자들의 합: 45
'''

n = 1
sum = 0
while n != 0:
    n = int(input("숫자를 입력하세요 (0을 입력하면 종료):"))
    sum += n

print(f"입력된 숫자들의 합: {sum}")
