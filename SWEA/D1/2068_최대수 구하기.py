T = int(input())

for test_case in range(1, T+1):
    num_arr = list(map(int, input().split()))

    result = 0
    for num in num_arr: # 배열을 순회하면서
        if num > result: # 배열의 값이 result보다 크다면
            result = num # 결과값에 배열의 값을 대입

    print('#{} {}'.format(test_case, result))
