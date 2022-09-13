def solution(d, budget):
    if sum(d) < budget:
        return len(d)
    else:
        d.sort()
        cnt = 0
        sum_money = 0
        for money in d:
            sum_money += money
            if sum_money <= budget:
                cnt += 1
            else:
                break
        return cnt