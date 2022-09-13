def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    same = []
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            same.append(i)

    for k in same:
        if k in lost:
            lost.pop(lost.index(k))

    answer = n - len(lost)
    for j in lost:
        if j-1 in reserve:
            reserve.pop(reserve.index(j-1))
            answer += 1
        elif j+1 in reserve:
            reserve.pop(reserve.index(j+1))
            answer += 1
    return answer