import heapq
def solution(scoville, K): #우선순위 큐 이용, heappop을 사용하면 가장 작은 값을 우선적으로 뽑을 수 있음
    answer = 0
    heapq.heapify(scoville) # 우선순위 큐
    while scoville:
        first = heapq.heappop(scoville) # 가장 낮은 스코필 뽑기
        if first >= K:
            break
        second = heapq.heappop(scoville) # 두번째로 낮은 스코필 뽑기
        heapq.heappush(scoville, first+second*2) # 섞어만든 스코필 넣기
        answer += 1
        if len(scoville) == 1 and scoville[0] < K: # 모든 음식을 섞은 후에도 K미만인 경우
            return -1
        
    return answer