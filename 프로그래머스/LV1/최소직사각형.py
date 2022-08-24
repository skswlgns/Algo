def solution(sizes):
    left_max = 0
    right_max = 0
    
    for i in sizes:
        i.sort()
        if i[0] > left_max: 
            left_max = i[0]
        if i[1] > right_max:
            right_max = i[1]

    return left_max * right_max