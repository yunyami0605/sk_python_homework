'''
문제 3-3 (중/하)
설명: 학생들의 성적을 딕셔너리로 저장하고 평균 점수를 계산하는 프로그램을 작성하세요.
 파일명: student_grades.py
 출력결과:
학생 성적:
김철수: 85점
이영희: 92점
박민수: 78점
최수진: 95점
평균 점수: 87.5점
'''

students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95   
}

sum = 0
avg = 0

for stu in students.keys():
    score = students[stu]
    sum += score
    print(f"{stu}: {score}점")

avg = sum / len(students.keys())
print(f"평균 점수: {avg:.1f}점")