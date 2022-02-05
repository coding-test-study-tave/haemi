import collections

def solution(arrows):
    answer = 0
    
    dirc = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1,-1)]
    way = {(0,0): []}
    
    now = (0,0)
    
    def saveway(a, now, delta):
        nonlocal answer
        
        if now not in way:
            way[now] = [a]
        else:
            way[now].append(a)
            
        now = (now[0] + delta[0], now[1] + delta[1])
        
        b = a-4 if a >= 4 else a+4 #진입한 경로
        if now not in way:
            way[now] = [b]
        else:
            if b not in way[now]:
                answer += 1
                way[now].append(b)

        return now
    
    for a in arrows:
        if abs(dirc[a][0]) + abs(dirc[a][1]) >= 2: #모래시계 형태를 처리하기 위해
            now = saveway(a, now, (dirc[a][0]/2, dirc[a][1]/2))
            now = saveway(a, now, (dirc[a][0]/2, dirc[a][1]/2))
        else:
            now = saveway(a, now, (dirc[a][0], dirc[a][1]))
        
    return answer