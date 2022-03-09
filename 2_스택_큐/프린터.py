from collections import deque
def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append(i)
    result=[]

    while True:
        pop_value=q.popleft()
        if priorities[pop_value] < max(priorities):
            q.append(pop_value)
        else:
            priorities[pop_value]=0
            result.append(pop_value)
            if pop_value==location:
                return len(result)