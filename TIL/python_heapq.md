# heap

1. 언제 사용하는가?

   ```
   원소들을 항상 정렬된 상태로 추가하고 삭제하고 싶을 때.
   
   heappush에서 가장 작은 값은 언제나 인덱스 0, 즉 이진트리의 루트에 위치
   
   ```

2. 사용방법

   ```python
   # 1) 모듈 임포트
   import heapq
   
   # 최소 힙 생성(리스트 생성)
   heap = []
   
   # 힙에 원소 추가
   heapq.heappush(heap, 12)
   heapq.heappush(heap, 7)
   heapq.heappush(heap, 23)
   heapq.heappush(heap, 1)
   
   print(heap)
   
   # out
   # [1, 7, 12, 23]
   
   print(heapq.heappop(heap))
   print(heap)
   
   # out
   # 1
   # [7, 12, 23]
   
   # 기존 리스트를 힙으로 변환
   List = [1, 7, 6, 13, 12]
   heapq.heapify(List)
   print(List)
   
   # out
   # [1, 6, 7, 12, 13]
   ```

   

3. 응용

   ```python
   # 1. 최대값
   import heapq
   
   nums = [4, 1, 7, 3, 8, 5]
   heap = []
   
   for num in nums:
       # 가장 큰 값의 음수는 가장 작은 값이므로 -를 붙여서 push해준다면 가장 큰 값부터 들어가게 된다.
       heapq.heappush(heap, (-num, num))
   
   
   while heap:
       # 두 번째 값을 뽑아내게 된다면 큰 값부터 확인을 할 수 있다.
       print(heapq.heappop(heap)[1])
       
   # out
   # 8
   # 7
   # 5
   # 4
   # 3
   # 1
   ```

   