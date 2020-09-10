import sys
sys.stdin = open('sample_input.txt', 'r')

def backtrack(selected,idx,input):
    global arr
    if idx == input:
        temp2 = []
        for i in range (input):
            if selected[i]:
                temp2.append(temp[i])
        arr.append(temp2)
        return arr

    else:
        selected[idx] = 1
        backtrack(selected,idx+1,input)

        selected[idx] = 0
        backtrack(selected, idx + 1, input)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    impossible = []
    for _ in range(M):
        impossible.append(sorted(list(map(int, input().split()))))

    temp = []
    for j in range(1, N+1):
        temp.append(j)

    arr = []
    backtrack([0] * N, 0, N)

    cnt = len(arr)

    for i in arr:
        t = []
        if len(i) > 2:
            for k in range(len(i)-1):
                for h in range(k+1, len(i)):
                    s = []
                    s.append(i[k])
                    s.append(i[h])
                    t.append(s)
            flag = True
            for z in impossible:
                if z in t:
                    flag = False

            if flag == False:
                cnt -= 1
        else:
            if i in impossible:
                cnt -= 1
    print('#{} {}'.format(test_case, cnt))