import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    friend_list = []
    for i in range(len(arr)):
        if arr[i][0] == 1:
            friend_list.append(arr[i][1])

    if len(friend_list) != 0:
        friend_friend_list = []
        for j in range(len(arr)):
            if arr[j][0] in friend_list:
                friend_friend_list.append(arr[j][1])
        result = len(set(friend_list + friend_friend_list))
    else:
        result = 0

    print('#{} {}'.format(test_case, result))

