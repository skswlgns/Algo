def solution(price, money, count):
    if sum([i for i in range(price, price*count+1, price)]) - money > 0:
        return sum([i for i in range(price, price*count+1, price)]) - money
    else:
        return 0