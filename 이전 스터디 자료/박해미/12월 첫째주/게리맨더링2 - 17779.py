#게리맨더링2
# 1.선거구 나눔
# 2.각 선거구를 나누는 갯수의 차이
# x,y,d1,d2==최대 N*N*N*N, 기준점=N*N => N^6
#[행][열]

#!/usr/bin/python3
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(d, x, y, g): 
    #bfs:임의의 정점 하나에서 시작해서, 모든 정점을 방문하는 알고리즘 (최단거리구하기)
    #정점과 간선 수 구해야 함, 시간복잡도=정점+간선
    #어떤곳을 방문했느지, 방문하지 않았는지 검사
    #dfs:스택 -> 인접리스트 방식으로 그래프 표현
    #bfs:큐 -> 인접리스트 방식으로 그래프 표현
    n = len(d)
    d[x][y] = g
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.pop() #now
        for k in range(4): #next
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == 0:
                    d[nx][ny] = g
                    q.append((nx,ny))

#bfs=너비우선탐색
#from collections import deque
# def bfs(graph, start, visted):
#   queue=deque([start]) 
#   visted[start]=True 현재노드 방문처리
#   while queue: 큐가 빌때까지 반복
#       v=queue.popleft()
#       for i in graph[v]: 아직 방문하지 않은 인접원소 큐에 삽입
#           if not visited[i]:
#               queue.append(i)
#               visited[i]=True 
# 
#dfs=깊이우선탐색
# def dfs(graph, v, visited):
#   visited[v]=True 현재노드 방문처리
#   for i in graph[v]:
#       if not visited[i]:
#           dfs(graph, i, visited)                    


def go(a, x, y, d1, d2): #구역나누는 함수
    n = len(a)
    d = [[0]*n for _ in range(n)]
    for i in range(0, d1+1):
        d[x+i][y-i] = 5 #왼쪽 상단 경계
        d[x+d2+i][y+d2-i] = 5 #오른쪽 하단 경계
    for i in range(0, d2+1): 
        d[x+i][y+i] = 5 #오른쪽 상단 경계
        d[x+d1+i][y-d1+i] = 5 #왼쪽 하단 경계

    for j in range(0, y-d1): #왼쪽 경계
        d[x+d1][j] = 3
    for i in range(0, x): #위쪽 경계
        d[i][y] = 1
    for j in range(y+d2+1, n): #아래쪽 경계
        d[x+d2][j] = 2
    for i in range(x+d1+d2+1, n): #오른쪽 경계
        d[i][y-d1+d2] = 4

    bfs(d, 0, 0, 1) #각각의 위치에서 bfs하면서 영역설정 해줌
    bfs(d, 0, n-1, 2)
    bfs(d, n-1, 0, 3)
    bfs(d, n-1, n-1, 4)
    cnt = [0]*5
    for i in range(n):
        for j in range(n):
            if d[i][j] == 0: #나머지는 5로 바꾸기
                d[i][j] = 5
            cnt[d[i][j]-1] += a[i][j] #각 칸의 인구수 구하기
    cnt.sort()
    ans = cnt[-1] - cnt[0] #최대-최소
    return ans


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ans = -1
for x in range(n):
    for y in range(n): #기준점 x,y
        for d1 in range(1, n):
            for d2 in range(1, n): #왼쪽은 d1, 오른쪽은 d2
                if 0 <= y-d1 and y+d2 < n: #각 격자의 양 끝 안에 d1,d2가 있는지
                    if x+d1+d2 < n:
                        temp = go(a, x, y, d1, d2) #구역나눈함수
                        if ans == -1 or ans > temp:
                            ans = temp

print(ans)