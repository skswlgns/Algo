import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    calculate_num = list(map(int, input().split()))
    num_arr = list(map(int, input().split()))

    