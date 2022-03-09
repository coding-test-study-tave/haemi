def solution(n, times):
    # 소요시간(=정답)의 min값과 max값을 정해두고 이 안에서 값의 범위를 좁혀가며 탐색
# 1. min, max 사이 중앙값 T을 구한다.
# 2. T시간 내 심사할 수 있는 사람의 수를 구한다.
# people += mid // time 을 통해서
# 3-1. 이 사람의 수가 n보다 크거나 같다면
# - 현재 mid값 내에서도 충분히 커버가 가능하기 때문에 최댓값을 mid-1으로 줄여준다.
# 3-2. 이 사람의 수가 n보다 작다면
# - 현재 mid값 내에서 커버가 불가하기 때문에 최솟값을 mid+1으로 높여준다.
    min_time = 1
    max_time = max(times)*n
    ans = 1
    while min_time <= max_time:
        mid = (min_time+max_time)//2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            ans = mid
            max_time = mid-1
        else:
            min_time = mid+1
    return ans