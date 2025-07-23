'''
문제 4-1 (하)
설명: 점수를 입력받아 학점을 출력하는 프로그램을 작성하세요. (90이상:A, 80이상:B, 70이상:C, 60이상:D, 미만:F)
 파일명: grade_calculator.py
 출력결과:
점수를 입력하세요: 85
점수 85점의 학점은 B입니다.
'''

score = int(input("점수를 입력하세요: "))

grade = "F"
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"

print(f"점수 {score}점의 학점은 {grade}입니다.")