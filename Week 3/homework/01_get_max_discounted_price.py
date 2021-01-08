# 나의 풀이

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 가격과 쿠폰을 내림차순으로 정렬
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    # 총 가격을 담을 변수
    total_price = 0

    for p,c in zip(prices, coupons):
        #zip 함수로 짝 지어진 가격&쿠폰을 계산하여 할인된 가격을 총 가격에 합산
        total_price += p * (1-c/100)
    # 쿠폰보다 물건 갯수가 더 많으므로 정가에 산 물건또한 계산
    total_price += prices[-(len(prices)-len(coupons))]

    # 정수형으로 출력
    return int(total_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.


# 강의 풀이 1

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    total_price = 0

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index])/100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return int(max_discounted_price)

print(get_max_discounted_price(shop_prices, user_coupons))