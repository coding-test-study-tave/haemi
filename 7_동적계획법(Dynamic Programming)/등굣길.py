def solution(m, n, puddles):
        # 1부터 시작하는 (1,1) ~ (n, m) 2차원 배열
    memo = [[0 for _ in range(m+1)] for _ in range(n+1)] # 0으로 초기화

    # 문제에서 주어지는 row, col는 반대라서 바꿔줌
    for col, row in puddles:
        memo[row][col] = -1 # 갈수 없는 물 웅덩이 표시
    memo[1][1] = 1 # 출발 지점 1로 지정

    def dp(row, col):
        if row < 1 or col < 1 or memo[row][col] < 0:
            return 0
        # 이미 계산한 값이 있으면 값을 바로 가져옴
        if memo[row][col] > 0:
            return memo[row][col]

        memo[row][col] = dp(row, col-1) + dp(row-1, col)
        return memo[row][col]

    return dp(n, m) % 1000000007