def solution(x):
    sum_of_numbers = 0
    for i in str(x):
        sum_of_numbers += int(i)    
    return x % sum_of_numbers == 0