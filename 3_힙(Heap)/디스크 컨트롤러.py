import heapq

def solution(jobs): #우선순위큐 이용
    #1.첫번째 작업이 시작하는 시간과 첫번째 작업이 끝나는 시간 사이에 들어온 요청들을 우선순위큐에 넣기
    #2.작업이 실행되는 시간동안 들어온 요청들에 대해, 현재 작업이 끝나는 시간까지 걸린 시간을 답에 더하기
    #3.우선순위큐를 pop()하여 작업에 소요되는 시간이 가장 작은 작업을 얻기
    #4.2번처럼 반복
    jobs.sort()
    answer = 0
    n = 0
    time = jobs[0][0] #최초 시간 설정
    pq = [] #우선순위 큐 생성
    while jobs:
        (request, expend) = jobs.pop(0) #jobs의 첫 원소 꺼내기
        n += 1
        time += expend #걸린 시간을 답에 더하기
        answer += (time - request) #요청 시간 request를 뺸 값 더하기
        
        while jobs and jobs[0][0] < time: #jobs가 비지 않고, jobs[0][0]일 떄 반복
            (request, expend) = jobs.pop(0)
            heapq.heappush(pq, (-expend, request))

        while pq:
            (expend, request) = heapq.heappop(pq)
            jobs.insert(0, [request, -expend])

    answer //= n
    return answer