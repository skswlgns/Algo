def solution(dartResult):
    answer = 0
    string_list = []
    string = dartResult[0]
    for i in range(1, len(dartResult)-1):
        string += dartResult[i]
        if dartResult[i+1].isdigit() == True:
            string_list.append(string)
            string = ''
        if i == len(dartResult)-2:
            string += dartResult[i+1]
            string_list.append(string)

    forbiden_list = ['0S#', '0S*', '0S', '0D#', '0D*', '0D', '0T#', '0T*', '0T']
    if len(string_list) > 3:
        for j in range(len(string_list)):
            if string_list[j] == '1':
                string_list[j] = '10'
            elif string_list[j] in forbiden_list:
                string_list[j] = string_list[j][1:]

        string_list[2] = string_list[2] + string_list[3]
        string_list.pop(3)
    
    for score in string_list:
        if len(score) == 2:
            if score[1] == 'S':
                answer += score[1]
            elif score[1] == 'D':
                answer += score[1]**2
            elif score[2] == 'T':
                answer += score[1]**3
    return answer

solution('1S2D*3T')
solution('1D2S#10S')
solution('1S*2T*3S')
solution('1D#2S*3S')
solution('1T2D3D#')
solution('1D2S3T*')
