'''
문제 8-3 (중/하)
설명: os와 sys 모듈을 사용하여 시스템 정보를 출력하고 파일 경로를 다루는 프로그램을 작성하세요.
 파일명: system_info.py
 출력결과:
현재 작업 디렉토리: /Users/username/python_practice
Python 버전: 3.9.7 (default, Oct 13 2021, 06:44:56)
운영체제: posix
환경 변수 PATH 일부: /usr/local/bin:/usr/bin:/bin
파일 경로 정보:
- 디렉토리: /Users/username/documents
- 파일명: report.txt
- 확장자: .txt
파일 존재 여부: False

'''

import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")

print(f"Python 버전: {sys.version}")

print(f"운영체제: {os.name}")

env_path = os.environ.get("PATH", "").split(":")
print("환경 변수 PATH 일부:", ":".join(env_path[:4]))

file = "/Users/cookie/coo/100_sk/homework/python/1_250721_파이썬연습문제/7_파일처리하기/log.txt"
dir = os.path.dirname(file)
fileName = os.path.basename(file)
_root, _ext = os.path.splitext(fileName)

print("파일 경로 정보:")
print(f"- 디렉토리: {dir}")
print(f"- 파일명: {fileName}")
print(f"- 확장자: {_ext}")
print("파일 존재 여부:", os.path.exists(file))