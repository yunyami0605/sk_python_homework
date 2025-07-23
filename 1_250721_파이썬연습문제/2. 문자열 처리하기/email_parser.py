'''
문제 2-3 (중/하)
설명: 이메일 주소를 입력받아 @ 기호를 기준으로 사용자명과 도메인을 분리하여 출력하는 프로그램을 작성하세요.
 파일명: email_parser.py
 출력결과:
이메일 주소를 입력하세요: user@example.com
사용자명: user
도메인: example.com
'''

email = input("이메일 주소를 입력하세요: ")
[name, domain] = email.split("@")

print(f"사용자명: {name}")
print(f"도메인: {domain}")