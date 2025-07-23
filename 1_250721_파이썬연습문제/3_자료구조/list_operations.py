'''
문제 3-9 (중/하)
설명: 두 개의 리스트를 병합하고 공통 요소를 찾는 프로그램을 작성하세요.
 파일명: list_operations.py
 출력결과:
리스트1: [1, 2, 3, 4, 5]
리스트2: [4, 5, 6, 7, 8]
병합된 리스트: [1, 2, 3, 4, 5, 6, 7, 8]
공통 요소: [4, 5]
'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = list(set(list1) | set(list2))
common = list(set(list1) & set(list2))

print(f"리스트1: {list1}")
print(f"리리스트2스트1: {list2}")
print(f"병합된 리스트: {list3}")
print(f"공통 요소: {common}")