from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    on_bridge_weight = 0
    
    # 트럭이 다리에 올라갈 때
    while bridge:
        answer += 1
        # 1. 기존 트럭이 나간다. 해당 무게를 제외
        on_bridge_weight -= bridge.popleft()
        
        if truck_weights:
            # 2. 트럭이 올라올 수 있는지 확인한다. 올라올 수 있는 경우 다리 위로 트럭을 올리고 무게를 증가
            if on_bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                on_bridge_weight += truck
                bridge.append(truck)
            # 3. 트럭이 올라올 수 없는 경우는 해당 트럭의 자리를 빈 자리로 두기
            else:
                bridge.append(0)

    return answer