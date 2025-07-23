'''
문제 6-3 (중/하)
설명: 기본값 매개변수를 사용하여 인사말을 생성하는 함수를 작성하세요.
 파일명: greeting_function.py
 출력결과:
안녕하세요, 김철수님!
Hello, John!
안녕하세요, 이영희님! 좋은 하루 되세요!

'''

def greeting(name, greeting="안녕하세요", other=""):
    print(f"{greeting}, {name}!{other}")

greeting("김철수님")
greeting("John", greeting="Hello", other="")
greeting("이영희님", other=" 좋은 하루 되세요")