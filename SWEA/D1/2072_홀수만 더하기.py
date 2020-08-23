T = int(input())

for test_case in range(T):
    numb_arr = list(map(int, input().split()))

    # 홀수일 경우 결과값을 더해줄 변수를 선언해줍니다.
    result = 0

    # 홀수인 경우만 추가해주는 것도 가능합니다.
    for num in numb_arr:
        if (num % 2) == 1: # 홀수일 경우
            result += num # result에 num값을 더해주어라.

    print('#{} {}'.format(test_case+1, result))