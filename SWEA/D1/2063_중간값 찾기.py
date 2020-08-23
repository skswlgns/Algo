T = int(input())

num_arr = list(map(int, input().split()))

num_arr.sort() # 낮은 숫자부터 높은 숫자로 정렬

middle = T // 2 # 중간 값의 위치

result = num_arr[middle] # 중간 값을 결과 값에 저장

print(result)
