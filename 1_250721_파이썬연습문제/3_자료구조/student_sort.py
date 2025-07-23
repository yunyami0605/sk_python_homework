'''
문제 3-10 (중/하)
설명: 학생 정보를 딕셔너리의 리스트로 저장하고 나이 순으로 정렬하는 프로그램을 작성하세요.
 파일명: student_sort.py
 출력결과:
나이 순으로 정렬된 학생 목록:
김철수 (20세) - 컴퓨터공학과
박민수 (21세) - 경영학과
이영희 (22세) - 영어영문학과
최수진 (23세) - 수학과

'''

mp = {
    "김철수": {
        "age": 20,
        "subject": "컴퓨터공학과"
    },

    "박민수": {
        "age": 21,
        "subject": "경영학과"
    },

    "이영희": {
        "age": 22,
        "subject": "영어영문학과"
    },

    "최수진": {
        "age": 23,
        "subject": "수학과"
    },
}

print("나이 순으로 정렬된 학생 목록:")

for name in mp.keys():
    _age = mp[name]["age"]
    _subject = mp[name]["subject"]

    print(f"{name} ({_age}세) - {_subject}")
    
