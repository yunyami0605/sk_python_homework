'''
문제 3-5 (중/하)
설명: 쇼핑 카트를 딕셔너리로 구현하여 상품을 추가하고 총 가격을 계산하는 프로그램을 작성하세요.
 파일명: shopping_cart.py
 출력결과:
쇼핑 카트:
사과: 2개 (개당 1000원) = 2000원
바나나: 3개 (개당 800원) = 2400원
오렌지: 1개 (개당 1500원) = 1500원
총 가격: 5900원
'''

shop = {
    "사과": {
        "count": 2,
        "price": 1000
    },
    "바나나": {
        "count": 3,
        "price": 800
    },
    "오렌지": {
        "count": 1,
        "price": 1500
    },
}

total = 0
for name in shop.keys():
    count = shop[name]["count"]
    price = shop[name]["price"]
    sum = count * price
    total += sum
    print(f'{name}: {count}개 (개당 {price}원) = {sum}원')

print(f'총 가격: {total}원')