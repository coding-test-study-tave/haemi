def solution(distance, rocks, n):
    rocks.append(distance) #도찰지점-바위 간의 거리도 포함하는 거니깐 distance를 넣어서 해결해줌
    rocks.sort() #오름차순 정렬
    
    left = 0 #최소거리는 0이다.
    right = distance #최대거리가 distance임으로
    
    while left <= right:
        mid = (left+right)//2
        current = 0 #현재 위치값
        min_distance = 0 #가장 작은 거리
        remove = 0 #제거할 바위 갯수
        
        for x in rocks:
            each_distance = x-current  # 바위인덱스 - 현재위치 = 사이 거리값
            if each_distance < mid: #거리값이 mid보다 작으면 바위를 제거해준다. 
                remove +=1 
            else: #거리값이 mid보다 크면 
                current = x #현재 위치를 바꾸고(그 전에꺼는 제거했단말)
                min_distance = min(min_distance, each_distance) #각 사이 거리 중에서도 최솟값을 구하는거라서 min으로 최솟값 갱신
                
        if remove > n: #제거한 바위가 n개 보다 많다면 -> mid를 줄여야된다는 의미 -> right을 줄여야됨
            right = mid-1 
        else: #제거한 바위가 n개보다 같거나 적다면 -> mid를 늘려야된다는 의미 & 최소거리 저장
            left = mid+1
            answer = min_distance
            
    return answer