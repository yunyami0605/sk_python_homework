'''
설명: enumerate를 사용하여 리스트의 인덱스와 값을 함께 출력하는 프로그램을 작성하세요.
 파일명: enumerate_example.py
 출력결과:
 과일 목록:
0: 사과
1: 바나나
2: 오렌지
3: 포도
4: 딸기
'''

tmp = ["사과", "바나나", "오렌지", "포도", "딸기"]

for idx, item in enumerate(tmp):
    print(f"{idx}: {item}")