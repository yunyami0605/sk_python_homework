'''
문제 1-2 (중/하)
설명: 원의 반지름을 입력받아 원의 넓이와 둘레를 계산하는 프로그램을 작성하세요. (π = 3.14159 사용)
'''

r = int(input("원의 반지름을 입력하세요: "))

area = 3.14 * r * r
circumference = 2 * 3.14 * r

print(f"반지름이 {r}인 원의 넓이: {area:0.2f}")
print(f"반지름이 {r}인 원의 둘레: {circumference:0.2f}")
