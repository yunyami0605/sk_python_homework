'''
문제 7-3 (중/하)
설명: 텍스트 파일의 단어 빈도를 계산하는 프로그램을 작성하세요.
 파일명: word_frequency.py
 출력결과:
단어 빈도 분석 결과:
파이썬: 3번
프로그래밍: 2번  
언어: 2번
배우기: 1번
쉬운: 1번
강력한: 1번
'''


with open("./test.txt", "r", encoding="utf-8") as file:
    test = {}

    lines = file.readlines()

    for line in lines:
        tmp = line.strip().split()
        print(tmp)
        for _tmp in tmp:
            test[_tmp] = test.get(_tmp, 0) + 1

    for _key, _value in test.items():
        print(f"{_key}: {_value}번")
    
        