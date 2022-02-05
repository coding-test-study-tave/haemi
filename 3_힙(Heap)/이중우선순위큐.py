import heapq
def solution(operations):
    pq = []#우선순위 큐(우선순위가 높은 데이터가 먼저 나옴, First in-First Out X)
    for operate in operations:
        (op, num) = operate.split(" ")# 1. 문자열 " " 기준으로 연산자와 숫자 나눔
        num = int(num)
        if op == 'I':
            heapq.heappush(pq, num)
            continue
        if not pq: #op == 'D'
            continue
        if num == -1:
            heapq.heappop(pq)
        else: #num == 1
            pq.remove(max(pq))

    answer = [max(pq), min(pq)] if pq else [0, 0] #최대최소 구함
    return answer