'''
문제 5-8 (중/하)
설명: 언패킹과 *args, **kwargs를 사용하는 예제를 작성하세요.
 파일명: unpacking_example.py
 출력결과:
좌표: x=10, y=20
리스트 언패킹: a=1, b=2, c=3
가변 인수의 합: 60
키워드 인수들: name=김철수, age=25, city=서울
'''

x, y = (10, 20)
print(f"좌표: x={x}, y={y}")

nums = [1, 2, 3]
a, b, c = nums
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def total(*args):
    return sum(args)

result = total(10, 20, 30)
print(f"가변 인수의 합: {result}")

def word(**kwargs):
    tmp = ""
    for key, value in kwargs.items():
        tmp += f"{key}={value}"
    print(f"키워드 인수들: {tmp}")

word(name="김철수", age=25, city="서울")
