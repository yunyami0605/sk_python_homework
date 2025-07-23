'''
문제 5-2 (중/하)
설명: 리스트에서 짝수만 추출하여 제곱하는 코드를 리스트 컴프리헨션으로 작성하세요.
 파일명: list_comprehension_example.py
 출력결과:
원본 리스트: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
짝수들: [2, 4, 6, 8, 10]
짝수의 제곱: [4, 16, 36, 64, 100]
'''

_origin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_even = [item for item in _origin if item % 2 == 0]
_even2 = [item ** 2 for item in _origin if item % 2 == 0]

print(f"원본 리스트: {_origin}")
print(f"짝수들: {_even}")
print(f"짝수의 제곱: {_even2}")