'''
문제 5-4 (중/하)
설명: zip을 사용하여 두 리스트를 결합하는 프로그램을 작성하세요.
 파일명: zip_example.py
 출력결과:
학생과 점수 매칭:
김철수: 85점
이영희: 92점
박민수: 78점
최수진: 95점
점수별 학생 딕셔너리: {'김철수': 85, '이영희': 92, '박민수': 78, '최수진': 95}


'''

students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

tmp = zip(students, scores)
for student, score in tmp:
    print(f"{student}: {score}점")


tmp2 = zip(students, scores)
print(f"점수별 학생 딕셔너리: {dict(tmp2)}")