def solution(prices):
    answer = []
    # 마지막은 항상 0으로 수렴하니까 마지막은 보지 않는다.
    for i in range(len(prices)-1):
        cnt = 0
        # 확인은 마지막까지 해준다.
        for j in range(i+1, len(prices)):
            # 자신보다 작은 값이 나올때 까지
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                # 자신보다 작은 값이 나오면 cnt + 1을 해주고 break
                cnt += 1
                break
        # answer에 cnt를 append해준다.
        answer.append(cnt)
    # 마지막은 항상 0이기에 0을 append
    answer.append(0)
    return answer