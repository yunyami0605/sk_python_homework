'''
2. 웹스크래핑 연습문제
2-1. Nate 뉴스기사 제목 스크래핑하기 (필수)
https://news.nate.com/recent?mid=n0100
최신뉴스, 정치 , 경제, 사회, 세계, IT/과학 
6개의 섹션의 뉴스를 출력하는 함수를 생성하여 스크래핑 하기

Image, 기사제목, 기사링크

뉴스기사의 Image를 출력 하세요 
1) Image의 절대경로와 상대 경로를 합치려면 urljoin 함수를 사용하세요.
    from urllib.parse import urljoin

2) Image 출력은 Image 클래스와 display 함수를 사용하세요.
    from IPython.display import Image, display

3) img 엘리먼트의 존재 여부를 체크하신 후에 src 속성의 이미지를 경로를 추출하기
  => Image 가 없는 뉴스도 있기 때문에 

'''
# <a href="//news.nate.com/view/20250722n33482?mid=n0300" class="lt1" onclick="ndrclick('RMG01');"></a>
# <img src="//thumbnews.nateimg.co.kr/news90///news.nateimg.co.kr/orgImg/mk/2025/07/22/20250723_01110105000003_L00.jpg" onerror="blankImg(this,0,0)" alt="">
from urllib.parse import urljoin
from IPython.display import Image, display
import requests
from bs4 import BeautifulSoup
base_url = "https://news.nate.com/recent?mid=n0"

req_header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

data = {
    "최신뉴스": "100",
    "정치": "200",
    "경제": "300",
    "사회": "400",
    "세계": "500",
    "IT/과학": "600",
}

# https://thumbnews.nateimg.co.kr/news90///news.nateimg.co.kr/orgImg/yt/2025/07/23/PRU20250718039401009_P2.jpg
def news_print():

    for _key, _value in data.items():
        url = f"{base_url}{_value}"
        res = requests.get(url, headers = req_header)   
        print(res.status_code)

        if res.ok:
            
            soup = BeautifulSoup(res.text, 'html.parser')


            news_wrapper = soup.select("div.mduSubjectList")

            print(news_wrapper)

            for news in news_wrapper[:6]:
                title = news.select_one("h2.tit")
                a_tag = news.select_one("a[href^='//news.nate.com/view']")
                img = news.select_one("img[src$='.jpg']")

                # Image, 기사제목, 기사링크
                print(f"기사제목: {title.text}")
                print(f"기사링크: http://{a_tag["href"]}")
                if img: print(f"Image: http://{img["src"]}")
                print("")


news_print()