T = int(input())

for test_case in range(1, T+1):
    num_arr = list(map(int, input().split()))

    result = 0 # 결과 값을 저장할 변수를 지정해줍니다.
    sum = 0 # 모두 더한 값을 저장할 변수를 지정해줍니다.

    for num in num_arr:
        sum += num # 배열에서 한 숫자씩 sum에 더해줍니다.
        result = sum/len(num_arr) # 더한 값에 배열의 길이를 나눠줍니다.

    print('#{} {}'.format(test_case, round(result))) # 결과 값은 반올림해주는 값이므로 round를 사용해줍니다.