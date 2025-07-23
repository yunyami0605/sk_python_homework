'''
문제 6-4 (중/하)
설명: 리스트의 통계 정보(평균, 최댓값, 최솟값, 표준편차)를 반환하는 함수를 작성하세요.
 파일명: statistics_function.py
 출력결과:
숫자들: [10, 20, 30, 40, 50]
평균: 30.0
최댓값: 50
최솟값: 10
표준편차: 15.81
'''
import numpy as np

def tmp(arr):
    return (sum(arr), max(arr), min(arr), np.std(arr))

arr = [10, 20, 30, 40, 50]
print(f"숫자들: {arr}")
print(f"평균: {tmp(arr)[0]}")
print(f"최댓값: {tmp(arr)[1]}")
print(f"최솟값: {tmp(arr)[2]}")
print(f"표준편차: {tmp(arr)[3]:.2f}")