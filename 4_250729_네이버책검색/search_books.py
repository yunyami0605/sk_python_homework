import requests
import os
import urllib.request
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")  # 개발자센터에서 발급받은 Client ID 값
client_secret = os.getenv("NAVER_CLIENT_SECRET") # 개발자센터에서 발급받은 Client Secret 값

req_header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret":  client_secret

}

def search_books(query):
    url = 'https://openapi.naver.com/v1/search/book.json'
    params = {
        'query': query,
        'display': 50,
        'sort': 'sim'
    }
    
    query_string = urllib.parse.urlencode(params)
    request_url = f"{url}?{query_string}"

    res = requests.get(request_url, headers=req_header)
    items_data = res.json()['items']

    os.makedirs('./data', exist_ok=True)
    
    # 1. 검색한 책 json으로 저장하기
    with open('./data/books.json', 'w', encoding='utf-8') as file:
        # file.write(items_data)
        json.dump(items_data, file, ensure_ascii=False, indent=2)

    # pandas로 csv로 저장
    df = pd.read_json('./data/books.json')

    # 읽어서 출력하기
    df.to_csv('./data/books.csv', index=False, encoding='utf-8-sig')
    print(df.head(50))


search_books("엔비디아")