def solution(n):
    string = list(str(n))
    answer = []
    for i in range(-1, -len(string)-1, -1):
        answer.append(int(string[i]))
    return answer