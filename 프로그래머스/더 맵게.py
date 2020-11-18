#  시간 초과가 난 코드(효율성 문제에서 걸림)

# def solution(scoville, K):
#     answer = 0
#
#
#
#     while True:
#         # 가장 낮은 값들이 먼저 나오게 정렬을 해줍니다.
#         if scoville[0] >= K:
#             break
#
#         if scoville[0] < K:
#             # 더한 수를 임시 변수에 저장
#             scov = scoville[0] + (scoville[1] * 2)
#             # 리스트 슬라이스 (첫 번째는 필요 없으니 없애주고 두 번째부터 리스트로 다시 생성해줍니다.)
#             scoville = scoville[1:]
#             scoville[0] = scov
#
#             answer += 1
#
#         if len(scoville) == 1 and scoville[0] < K:
#             answer = -1
#             break
#     return answer

import heapq

def solution(scoville, K):
    answer = 0

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if heap[0] >= K:
            break
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))

        answer += 1
        if len(heap) == 1 and heap[0] < K:
            answer = -1
            break

    return answer