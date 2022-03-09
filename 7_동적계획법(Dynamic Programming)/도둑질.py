def solution(money):
    answer = 0
    # 마지막집을 선택하지 않은경우
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    answer = max(answer, max(dp))

    #첫번째 집을 선택하지 않은 경우
    dp = [0] * len(money)
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    answer = max(answer, max(dp))
    
    return answer