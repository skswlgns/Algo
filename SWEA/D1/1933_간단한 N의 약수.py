import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for i in range(1, test_case+1):
    if test_case % i == 0:
        print(i, end=" ")