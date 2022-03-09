def solution(n, lost, reserve):   
    
    lost = set(lost)
    reserve = set(reserve)
    # 여벌체육복을 가져온 학생이 체육복을 도난당했을경우 reserve에서 제외
    
    common = lost & reserve
    lost = list(lost - common)
    reserve = list(reserve - common)
    
    reserve.sort()
    
    for i in reserve:
        a,b = i-1, i+1
        if a in lost:
            lost.remove(a)
            continue
        if b in lost:
            lost.remove(b)
    
    return n-len(lost)