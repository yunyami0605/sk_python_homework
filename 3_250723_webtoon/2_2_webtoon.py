'''
2-2. 하나의 네이버 웹툰과 1개의 회차에 대한 Image 다운로드 하기 (필수)
:  하나의 웹툰의 제목(title)과 회차번호(no),회차의URL(url) 을 입력으로 받는 함수를 선언합니다. 
   def download_one_episode(title,no,url):

아래와 같이 호출합니다.
download_one_episode('낢이사는이야기',48,'https://comic.naver.com/webtoon/detail?titleId=833255&no=49&week=tue')

img\낢이사는이야기\48 디렉토리가 생성되며 , 
그 디렉토리 아래에 웹툰 image들이 다운로드 되도록 해주세요.
'''

import requests
from bs4 import BeautifulSoup
import os

def download_one_episode(title, no, url):
    req_header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        'referer': url,
    }

    res = requests.get(url, headers=req_header)

    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')

        imgs = soup.select("img[src*='_IMAG01_']")  # 일반적으로 이 패턴에 포함됨

        # 폴더 만들기
        folder_path = f'./img/{title}/{no}'
        os.makedirs(folder_path, exist_ok=True)

        for idx, img_tag in enumerate(imgs[:10], 1):
            img_url = img_tag["src"]
            img_data = requests.get(img_url, headers=req_header).content

            ext = os.path.splitext(img_url)[1].split('?')[0] or '.jpg'
            file_name = f'{idx:02d}{ext}'
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "wb") as file:
                file.write(img_data)


# 예시 호출
download_one_episode(
    '낢이사는이야기',
    48,
    'https://comic.naver.com/webtoon/detail?titleId=817752&no=1&week=fri'
)
