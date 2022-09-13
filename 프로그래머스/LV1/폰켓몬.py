def solution(a):
    if len(a)/2 > len(set(a)):
        return int(len(set(a)))
    else:
        return int(len(a))/2