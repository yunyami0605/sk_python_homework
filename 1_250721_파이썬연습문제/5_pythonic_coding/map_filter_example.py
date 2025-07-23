'''
문제 5-7 (중/하)
설명: map과 filter를 사용하여 리스트를 처리하는 프로그램을 작성하세요.
 파일명: map_filter_example.py
 출력결과:
원본 숫자: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
모든 수의 제곱: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
5보다 큰 수들: [6, 7, 8, 9, 10]
5보다 큰 수들의 제곱: [36, 49, 64, 81, 100]
'''

origin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x2 = list(map(lambda x: x ** 2, origin))
g5 = list(filter(lambda x: x > 5, origin))
g52 = list(map(lambda x: x ** 2, g5))

print(f"원본 숫자: {origin}")
print(f"모든 수의 제곱: {x2}")
print(f"5보다 큰 수들: {g5}")
print(f"5보다 큰 수들의 제곱: {g52}")