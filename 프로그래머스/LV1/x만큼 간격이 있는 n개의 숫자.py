### 피드백 전 나의 코드
def solution(x, n):
    answer = []

    answer.append(x)
    result = x
    for _ in range(n-1):
        result += x 
        answer.append(result)

    return answer

### 피드백 후 코드
def solution(x, n):
    answer = [(i+1)*x for i in range(n)]
        
    return answer