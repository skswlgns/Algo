T = int(input())

for test_case in range(1, T+1):
    num_x, num_y = map(int, input().split())

    result = '' # 결과값을 저장해줄 변수를 지정
    # 왼쪽 수가 오른쪽 수보다 큰 경우
    if num_x > num_y:
        result = '>'
    # 오른쪽 수가 더 큰 경우
    elif num_x < num_y:
        result = '<'
    # 같을 경우
    else:
        result = '='

    print('#{} {}'.format(test_case, result))