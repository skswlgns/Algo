person1 = [1, 2, 3, 4, 5]
person2 = [2, 1, 2, 3, 2, 4, 2, 5]
person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    result = {'1': 0, '2': 0, '3': 0}
    for i in range(len(answers)):
        num1 = i % len(person1)
        num2 = i % len(person2)
        num3 = i % len(person3)

        if answers[i] == person1[num1]:
            result['1'] += 1
        if answers[i] == person2[num2]:
            result['2'] += 1
        if answers[i] == person3[num3]:
            result['3'] += 1 

    sort_result = sorted(result.items(), key=lambda x:x[1])
    if sort_result[2][1] == sort_result[1][1]:
        if sort_result[2][1] == sort_result[0][1]:
            return [1, 2, 3]
        else:
            return [int(sort_result[1][0]), int(sort_result[2][0])]
    else:
        return [int(sort_result[2][0])]