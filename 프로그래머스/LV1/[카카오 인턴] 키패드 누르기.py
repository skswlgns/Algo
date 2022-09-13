numbers_dict = {'1': (0, 0, 'left'), '2': (0, 1, 'middle'), '3': (0, 2, 'right'),
                '4': (1, 0, 'left'), '5': (1, 1, 'middle'), '6': (1, 2, 'right'),
                '7': (2, 0, 'left'), '8': (2, 1, 'middle'), '9': (2, 2, 'right'),
                '*': (3, 0, 'left'), '0': (3, 1, 'middle'), '#': (3, 2, 'right')}

def solution(numbers, hand):
    answer = ''
    hand = 'L' if hand=='left' else 'R'
    left  = numbers_dict['*']
    right = numbers_dict['#']

    for i in numbers:
        tuple_i = numbers_dict[str(i)]
        if tuple_i[2] == 'middle':
            left_dist  = abs(tuple_i[0]-left[0]) + abs(tuple_i[1]-left[1])
            right_dist = abs(tuple_i[0]-right[0]) + abs(tuple_i[1]-right[1])

            if left_dist > right_dist:
                answer += 'R'
                right = numbers_dict[str(i)]
            elif left_dist < right_dist:
                answer += 'L'
                left = numbers_dict[str(i)]
            else:
                answer += hand
                if hand == 'L':
                    left = numbers_dict[str(i)]
                else:
                    right = numbers_dict[str(i)]

        elif tuple_i[2] == 'left':
            answer += 'L'
            left = numbers_dict[str(i)]
        else:
            answer += 'R'
            right = numbers_dict[str(i)]

    return answer