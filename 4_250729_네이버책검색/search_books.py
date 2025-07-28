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
    
    # 1. 검색어로  찾은  책 목록을 json 파일로 저장하기
    with open('./data/books.json', 'w', encoding='utf-8') as file:
        # file.write(items_data)
        json.dump(items_data, file, ensure_ascii=False, indent=2)

    # 2.  books.json 파일을 Pandas DataFrame로 저장하기
    df = pd.read_json('./data/books.json')
    df.to_csv('./data/books.csv', index=False, encoding='utf-8-sig')

    # 3. 검색어로  찾은  책 목록 출력하기

    books = pd.DataFrame(items_data)
    print(books.head(50))

    # discount 컬럼을 숫자로 변환 (에러 방지용)
    books['discount'] = pd.to_numeric(books['discount'], errors='coerce')

    # 4. 검색어로  찾은  책 목록 중에서 가격이 2만원 이상인 책만 출력하기
    filtered_books = books.loc[books['discount'] > 20000, ["title", "author", "discount", "publisher", "pubdate"]] \
                        .sort_values(by='discount', ascending=False) \
                        .reset_index(drop=True)
    print(filtered_books)
    
    # 6. 질문 :  검색어로  찾은  책 목록 중에서 출판사가 인피니티북스인 책만 출력하기
    filtered_books2 = books.loc[books['publisher'] == "인피니티북스", [col for col in df.columns if col not in ['image', 'description']] ] \
                        .reset_index(drop=True)
    print("@ filtered_books2")
    print(filtered_books2)

    # 6. 질문 :  검색어로  찾은  책 목록 중에서 출판사가 인피니티북스인 책만 출력하기




search_books("엔비디아")