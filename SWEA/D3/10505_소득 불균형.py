for test_case in range(1, T+1):
    population = int(input())
    people_money = list(map(int, input().split()))

    sum_money = 0 # 사람들이 가지고 있는 돈을 합산하기 위한 변수를 지정
    for i in people_money:
        sum_money += i

    average = sum_money / population # 합산한 돈에서 인구 수를 나누어줌

    result = 0 # 결과 값을 대입해줄 변수를 지정

    for j in people_money:
        if j <= average: # 만약 평균이하의 돈을 가지고 있다면
            result += 1 # 결과 값에 1을 더하여라

    print('#{} {}'.format(test_case, result))