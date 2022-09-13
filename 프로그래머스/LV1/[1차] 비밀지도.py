def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        if len(format(arr1[i], 'b')) < n:
            first = '0'*(n-len(format(arr1[i], 'b'))) + format(arr1[i], 'b')
        else:
            first = format(arr1[i], 'b')
        if len(format(arr2[i], 'b')) < n:
            second = '0'*(n-len(format(arr2[i], 'b'))) + format(arr2[i], 'b')
        else:
            second = format(arr2[i], 'b')
        
        tmp = ''
        for j in range(n):
            if first[j] == '1' or second[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer