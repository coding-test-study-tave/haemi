#DFS
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int,input().split())
a = [[] for _ in range((n+1))]
check = [False] * (n+1)
for _ in range(m):
    x, y = map(int,input().split())
    a[y].append(x)

def go(x):
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            go(y)
    print(x, end=' ')
    
for i in range(1, n+1):
    if check[i] == False:
        go(i)
        
print()


#BFS
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
a = [[] for _ in range((n+1))]
ind = [0] * (n+1)
for _ in range(m):
    x, y = map(int,input().split())
    a[x].append(y)
    ind[y] += 1

q = deque()

for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end = ' ')
    for y in a[x]:
        ind[y] -= 1
        if ind[y] == 0:
            q.append(y)

print()