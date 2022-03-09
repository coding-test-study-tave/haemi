def solution(prices):
    maxIndex = len(prices) - 1
    answer =  [0] * (maxIndex + 1)
    for idx, price in enumerate(prices) :
        cnt = idx
        for i in range(maxIndex - idx) :
            cnt += 1
            if(not price <= prices[cnt]) :
                answer[idx] = cnt - idx
                break
            answer[idx] = cnt - idx
    return answer