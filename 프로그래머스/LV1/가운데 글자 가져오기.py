def solution(s):
    middle = round(len(s)/2+0.1)
    if len(s) % 2 == 0:
        return s[middle-1:middle+1]
    else:
        return s[middle-1]