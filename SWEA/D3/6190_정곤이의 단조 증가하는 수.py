T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    num_arr = list(map(int, input().split()))

    multi = []
    for i in range(N-1):
        for j in range(i+1, N):
            multi.append(num_arr[i] * num_arr[j])

    multi.sort(reverse=True)

    for i in multi:
        i = str(i)
        flag = True
        for j in range(len(i)-1):
            if i[j] > i[j+1]:
                flag = False
        if flag == True:
            result = i
            break

    if flag == False:
        result = -1

    print('#{} {}'.format(test_case, result))
