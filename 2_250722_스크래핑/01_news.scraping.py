'''
    질문1 :  아래의 url에서 뉴스기사의 링크와 제목을 출력하세요.
    # 다음 경제 뉴스 URL
    url = 'https://news.daum.net/economy'
'''

import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/economy" 

reqHeader = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}


res = requests.get(url, reqHeader)
res.encoding = 'utf-8'

if res.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    aTags = soup.select("a.item_newsheadline2[href^='https://v.daum.net/v/']")

    titles = soup.select("a.item_newsheadline2[href^='https://v.daum.net/v/'] .tit_txt")

    for at in aTags:
        _url = at.get("href")
        titleTag = at.select_one('div.cont_thumb strong.tit_txt')
        _title = titleTag.text.strip()
        print(_url)
        print(_title)

    

'''
질문2:  여러개의 section 중 하나를 선택해서 url에서 뉴스기사의 링크와 제목을 출력하는 코드를 함수로 작성하기

'''

url2 = 'https://news.daum.net/'

section_dict = {'기후/환경':'climate','사회':'society','경제':'economy','정치':'politics',\
             '국제':'world','문화':'culture','생활':'life','IT/과학':'tech','인물':'people'}



def print_news(section_name):
    val = section_dict[section_name]
    print(f"======> https://news.daum.net/{val} {section_name} 뉴스 <======")

    _url2 = f"https://news.daum.net/{val}" 

    reqHeader = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }


    res = requests.get(_url2, reqHeader)
    res.encoding = 'utf-8'

    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        aTags = soup.select("a.item_newsheadline2[href^='https://v.daum.net/v/']")

        titles = soup.select("a.item_newsheadline2[href^='https://v.daum.net/v/'] .tit_txt")

        for at in aTags:
            _url = at.get("href")
            titleTag = at.select_one('div.cont_thumb strong.tit_txt')
            _title = titleTag.text.strip()
            print(_url)
            print(_title)

print_news('경제')
print_news('사회')
