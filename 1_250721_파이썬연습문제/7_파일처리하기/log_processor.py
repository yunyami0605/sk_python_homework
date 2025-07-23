'''
문제 7-5 (중/하)
설명: 로그 파일을 생성하고 특정 레벨의 로그만 필터링하여 출력하는 프로그램을 작성하세요.
 파일명: log_processor.py
 출력결과:
로그 파일이 생성되었습니다.

ERROR 레벨 로그들:
2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음

WARNING 레벨 로그들:  
2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족
'''

logs = [
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족",
]

with open("log.txt", "w", encoding="utf-8") as file:
    for log in logs:
        file.write(log + "\n")

print("로그 파일이 생성되었습니다.\n")

with open("log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("ERROR 레벨 로그들:")
for line in lines:
    if "ERROR" in line:
        print(line.strip())

print("WARNING 레벨 로그들:")
for line in lines:
    if "WARNING" in line:
        print(line.strip())