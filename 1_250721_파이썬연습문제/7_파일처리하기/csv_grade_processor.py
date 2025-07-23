'''
설명: CSV 형태의 학생 성적 데이터를 파일에 저장하고 읽어서 평균을 계산하는 프로그램을 작성하세요.
 파일명: csv_grade_processor.py
 출력결과:
학생 성적이 grades.csv에 저장되었습니다.

성적 분석 결과:
김철수: 85점
이영희: 92점  
박민수: 78점
최수진: 95점
전체 평균: 87.5점
'''

import csv

grades = [
    ["김철수", 85],
    ["이영희", 92],
    ["박민수", 78],
    ["최수진", 95],
]

with open("grades.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "점수"])  # 헤더
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.")

total = 0
count = 0

print("성적 분석 결과:")

with open("grades.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    #파일을 한줄씩 읽음
    next(reader) 

    for row in reader:
        name, score = row[0], int(row[1])
        print(f"{name}: {score}점")
        total += score
        count += 1

average = total / count
print(f"전체 평균: {average:.1f}점")