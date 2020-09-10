for test_case in range(1, T+1):
    # N 총 명수, P - P채널 구독자, T - T 채널 구독자
    N, P, T = map(int, input().split())

    # 최대값은 구하기 편하다.(P,T중 작은 값이 곧 최대값이 된다.)
    if P >= T :
        max_intersec = T
    elif P <= T:
        max_intersec = P

    # 최소값을 구하는 중 N보다 P,T의 합이 작다면 최소값은 항상 0이 된다.
    if N >= (P+T):
        min_intersec = 0
    else:
        min_intersec = (P+T) - N

    print('#{} {} {}'.format(test_case, max_intersec, min_intersec))