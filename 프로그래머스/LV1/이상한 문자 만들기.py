def solution(s):
    answer = ''
    for split_string in s.split(' '):
        for i in range(len(split_string)):
            if i % 2 == 0:
                answer += split_string[i].upper()
            else:
                answer += split_string[i].lower()
        answer += ' '
    return answer[:-1]
