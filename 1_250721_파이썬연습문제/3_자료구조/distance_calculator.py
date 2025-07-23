'''
문제 3-4 (중/하)
설명: 좌표를 튜플로 저장하고 두 점 사이의 거리를 계산하는 프로그램을 작성하세요.
 파일명: distance_calculator.py
 출력결과:
점1: (0, 0)
점2: (3, 4)
두 점 사이의 거리: 5.0
'''
import math


site1 = (0, 0)
site2 = (3, 4)


distance = math.sqrt((site2[0] - site1[0]) ** 2 + (site2[1] - site1[1]) ** 2)

print(f"점1: {site1[0], site1[1]}")
print(f"점2: {site2[0], site2[1]} ")
print(f"두 점 사이의 거리:  {distance}")