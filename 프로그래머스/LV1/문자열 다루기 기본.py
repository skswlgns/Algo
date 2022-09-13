def solution(s):
    if 4 == len(s) or len(s) == 6:
        try:
            int(s)
            return True
        except:
            return False
    else:
        return False    