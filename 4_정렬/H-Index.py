def solution(citations):
    answer = 0
    # 1. citations을 오름차순으로 정렬
    citations.sort()
    # 2. citations 길이 n을 구함
    n = len(citations)
    # 3. 0~n까지 다음을 반복
    for i in range(n):
        # 1. hIndex는 n-i
        hIndex = n-i
        # 2. citations[i]가 hIndex보다 크거나 같으면, answer에 hIndex를 저장하고 반복을 멈춤
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer