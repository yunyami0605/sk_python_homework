'''
문제 7-4 (중/하)
설명: JSON 형태의 데이터를 파일에 저장하고 읽어오는 프로그램을 작성하세요.
 파일명: json_handler.py
 출력결과:
데이터가 data.json에 저장되었습니다.

JSON에서 읽어온 데이터:
이름: 김철수
나이: 25
직업: 개발자
취미: ['독서', '영화감상', '코딩']
주소: 서울시 강남구

'''
import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ['독서', '영화감상', '코딩'],
    "주소": "서울시 강남구"
}

with open("data.json", "w", newline="", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
    
print("데이터가 data.json에 저장되었습니다.")

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("JSON에서 읽어온 데이터:")
print(f"이름: {loaded_data['이름']}")
print(f"나이: {loaded_data['나이']}")
print(f"직업: {loaded_data['직업']}")
print(f"취미: {loaded_data['취미']}")
print(f"주소: {loaded_data['주소']}")