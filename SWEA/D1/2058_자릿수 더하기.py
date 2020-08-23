T = str(input()) # 문자여롤 받아오면 각 자릿수를 더하기 쉬우니 문자열로 받아온다.

result = 0

for num in T:
    result += int(num)

print(result)