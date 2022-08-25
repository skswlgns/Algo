def solution(lottos, win_nums):
    equal_num = 0
    for lotto in lottos:
        if lotto in win_nums:
            equal_num += 1

    win = 7
    if equal_num >= 2:  
        if lottos.count(0) > 0:
            answer = [win - equal_num - lottos.count(0), win-equal_num]
        else:
            answer = [win - equal_num, win-equal_num]

    else:
        if equal_num == 1:
            if lottos.count(0) > 0:
                answer = [win-lottos.count(0)-equal_num, 6]
            else:
                answer = [6, 6]
        else:
            if lottos.count(0) > 1:
                answer = [win-lottos.count(0), 6]
            else:
                answer = [6, 6]

    return answer