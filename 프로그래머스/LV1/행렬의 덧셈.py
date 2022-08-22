def solution(arr1=[[1],[2]], arr2=[[4],[6]]):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr1[i])):
            result.append(arr1[i][j]+arr2[i][j])
        answer.append(result)            
    return answer