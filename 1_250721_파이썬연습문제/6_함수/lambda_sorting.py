'''
문제 6-5 (중/하)
설명: 람다 함수를 사용하여 리스트를 다양한 방식으로 정렬하는 프로그램을 작성하세요.
 파일명: lambda_sorting.py
 출력결과:
학생 정보: [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]
이름순 정렬: [('김철수', 85), ('박민수', 78), ('이영희', 92), ('최수진', 95)]
점수순 정렬: [('박민수', 78), ('김철수', 85), ('이영희', 92), ('최수진', 95)]
점수 내림차순: [('최수진', 95), ('이영희', 92), ('김철수', 85), ('박민수', 78)]
'''

stud = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]
name = list(stud)
score = list(stud)
scoreDown = list(stud)
name.sort( key=lambda x: x[0])
score.sort(key=lambda x: x[1])
scoreDown.sort( key=lambda x: x[1], reverse = True)

print("학생 정보:", stud)
print("이름순 정렬:", name)
print("점수순 정렬:", score)
print("점수 내림차순:", scoreDown)
