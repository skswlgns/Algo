def solution(survey, choices):
    type_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    choice_list = [-3, -2, -1, 0, 1, 2, 3]
    check_list  = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    for i in range(len(survey)):
        if choice_list[choices[i]-1] > 0:
            type_dict[survey[i][1]] += choice_list[choices[i]-1]
        elif choice_list[choices[i]-1] < 0:
            type_dict[survey[i][0]] += abs(choice_list[choices[i]-1])
    answer = ''
    for j in check_list:
        if type_dict[j[0]] > type_dict[j[1]]:
            answer += j[0]
        elif type_dict[j[0]] < type_dict[j[1]]:
            answer += j[1]
        else:
            answer += j[0]
    
    return answer