def solution(progresses, speeds):
    answer = []
    day = 1 # 날짜를 새는 변수
    count = 0 # 작업 완료된 기능을 카운트 하는 변수
    
    # 모든 기능이 완료되어 남은 기능이 없을때까지 반복
    while len(progresses) > 0:
    	# 뒤의 기능이 완료가 되어도 앞의 기능이 완료되어야 배포가 가능하기 때문에 리스트의 첫번째 요소로 비교
        if progresses[0] + (day * speeds[0]) >= 100:
            # 기능이 완료되면 첫번째 요소를 제거
            progresses.pop(0)
            speeds.pop(0)
            
            # 완료된 기능 카운트
            count += 1
        else:
	        # 완료된 기능이 있을경우 answer에 count를 넣고 count를 0으로 초기화
            # 완료된 기능이 없을경우 날짜를 +1
            if count > 0:
                answer.append(count)
                count = 0
            else:
                day += 1
	# 마지막 기능이 완료되면 안의 else문을 타지 않고 while문이 종료 되기 때문에 마지막 기능까지 추가
    answer.append(count)
    return answer