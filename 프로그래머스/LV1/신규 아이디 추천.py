import string
def solution(new_id):
    allow_list = [x for x in string.ascii_lowercase] + [str(x) for x in range(0, 10)] + ['-', '_', '.']
    
    id = ''
    for word in new_id:
        if word.lower() in allow_list:
            id += word.lower()

    id = id.strip('.')
    if len(id) > 0:
        while True:
            id = id.replace('..', '.')
            if id.find('..') == -1:
                break
    
    answer = id
    if len(id) > 15:
        id = id[:15]
        answer = id.rstrip('.')
    elif len(id) < 3:
        if len(id) == 0:
            answer = 'aaa'
        else:
            answer = id
            while True:
                if len(answer) == 3:
                    break
                answer += id[-1]
    print(answer)
    return answer