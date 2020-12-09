def solution(number, k):
    K = len(number)-k
    # 슬라이싱을 사용하여 풀 예정입니다.
    answer = 0
    for i in range(len(number)-K+1):
        for j in range(i+1, len(number)):
            if not (j+K-1) > len(number):
                if answer < int(number[i]) + int(number[j:j+K-1]):
                    answer = int(number[i]) + int(number[j:j+K-1])
    answer = str(answer)
    print(answer)
    return answer

solution("1231234", 3)