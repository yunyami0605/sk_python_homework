'''
문제 5-1 (중/하)
설명: 문자열을 단어별로 분리했다가 다시 합치는 코드를 split과 join을 사용하여 작성하세요.
 파일명: split_join_example.py
 출력결과:
원본 문자열: Python is awesome programming language
분리된 단어들: ['Python', 'is', 'awesome', 'programming', 'language']
하이픈으로 연결: Python-is-awesome-programming-language
대문자로 변환 후 공백으로 연결: PYTHON IS AWESOME PROGRAMMING LANGUAGE

'''

_origin = "Python is awesome programming language"

_split = _origin.split(" ")
_join = "-".join(_split)
_upper = " ".join(_split).upper()

print(f"원본 문자열: {_origin}")
print(f"분리된 단어들: {_split}")
print(f"하이픈으로 연결: {_join}")
print(f"대문자로 변환 후 공백으로 연결: {_upper}")