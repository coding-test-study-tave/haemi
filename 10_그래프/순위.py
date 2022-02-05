from collections import Counter

def solution(n, results):
    board = [[0]*(n) for _ in range(n)]
    for p1, p2 in results:
        board[p1 - 1][p2 - 1] = 1 #p1이 이기면 1
        board[p2 - 1][p1 - 1] = -1 #p1이 지면 -1
    print('채워지기 전')
    print(board)

    #확실하지 않은 부분 (0)을 채워나가기
    for k in range(n):                 
        for i in range(n):              
            for j in range(n):          
                if board[i][j] == 0:   
                    if board[i][k] == 1 and board[k][j] == 1: #i>k>j
                        board[i][j] = 1
                    elif board[i][k] == -1 and board[k][j] == -1: #i<k<j
                        board[i][j] = -1
    print('채워진 후')
    print(board)
    ans = 0
    for i in range(n): #!!
        if Counter(board[i])[0] == 1:
            ans += 1

    return ans