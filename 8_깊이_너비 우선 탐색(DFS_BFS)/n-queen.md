# [백준] dfs/bfs - 양
https://www.acmicpc.net/problem/3184

## 문제 접근 
> 백트레킹이 어려워서 처음부터 답을 보고 이해했다. 같은 열에는 무조건 한개의 queen이있고 대각선, 열에 같은게 존재하지 않는지를 체크하고 없으면 다시 재귀로 dfs로 풀어야된다. 인터넷 검색해서 나오는 풀이들 python으로 재출했을때 죄다 시간초과가 뜨고 pypy3로 재출했을때도 시간초과, 런타임에러가 난다. pypy3로 재출해서 통과된 코드로 공부해보았다. 

## 코드
```python
s = int(input())
queen = [0]*s # queen[i] = j의 의미는 [i, j]에 queen말을 놓는다고 생각하면됨

def dfs(queen, row, n):
    count = 0 #말을 놓을 수 있는 갯수
    if row == n: # row가n이라는 의미는 각 row별로 알맞은 말을 놓았다는 의미로 퀸을 놓는 방법이라는 의미
        return 1
    
    for col in range(n): # 같은행에서 각각 컬럼에 말을 놓기
        queen[row] = col
        for i in range(row): # 다음 row를 탐색하면 말을 놓을 수 있는 조건(같은열, 같은 대각선아닌거) 보기
            if queen[row] == queen[i] or abs(queen[row]-queen[i]) == abs(row-i):
                break
        else:
            count+=dfs(queen, row+1, n) #같은 열, 같은 대각선이 아니면 다음줄(row)에 말을 놓을 자리 탐색  
    return count

print(dfs(queen, 0, s))     
```
