'''
문제 8-2 (중/하)
설명: datetime과 random 모듈을 사용하여 임의의 날짜와 숫자를 생성하는 프로그램을 작성하세요.
 파일명: module_usage.py
 출력결과:
현재 날짜와 시간: 2025-07-20 14:30:25
포맷된 날짜: 2025년 07월 20일 일요일
임의의 숫자: 7
임의의 실수: 3.14
임의의 리스트 요소: 바나나
섞인 리스트: ['포도', '사과', '오렌지', '바나나', '딸기']

'''

import datetime
import random

tmp = datetime.datetime.now()
print("현재 날짜와 시간:", tmp.strftime("%Y-%m-%d %H:%M:%S"))

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
tmp2 = tmp.strftime(f"%Y년 %m월 %d일 {weekdays[tmp.weekday()]}")
print("포맷된 날짜:", tmp2)

print("임의의 숫자:", random.randint(1, 100))
print("임의의 실수:", round(random.uniform(1.0, 100.0), 2))

fruits = ['포도', '사과', '오렌지', '바나나', '딸기']
print("임의의 리스트 요소:", random.choice(fruits))

random.shuffle(fruits)
print("섞인 리스트:", fruits)