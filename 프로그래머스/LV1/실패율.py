def solution(N, stages):
    stages.sort()
    
    stage_count = []
    for i in range(1, N+1):
        if len(stages) > 0:
            a = stages.count(i)
            stage_count.append((i, a/len(stages)))
            stages = stages[a:]
        else:
            stage_count.append((i, 0))
    
    answer = []
    for i in sorted(stage_count, key=lambda x:x[1], reverse=True):
        answer.append(i[0])

    return answer