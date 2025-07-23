'''
문제 3-1 (하)
설명: 5개의 숫자를 리스트에 저장하고 합계와 평균을 구하는 프로그램을 작성하세요.
 파일명: list_statistics.py
 출력결과:
숫자들: [10, 20, 30, 40, 50]
합계: 150
평균: 30.0

'''

arr = [10, 20, 30, 40, 50]

sum = 0
avg = 0

for item in arr:
    sum += item
    avg = sum / len(arr)

print(f"합계: {sum}")
print(f"평균: {avg:.1f}")