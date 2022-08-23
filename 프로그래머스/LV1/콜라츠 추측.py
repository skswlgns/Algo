def solution(num):
    if num == 1:
        return 0
    answer = 0
    while answer < 501:
        if num % 2 == 0:
            num /= 2
        else:
            num = (num*3)+1
        answer += 1
        
        if num == 1:
            break
            
    if answer <= 500:
        return answer
    else:
        return -1