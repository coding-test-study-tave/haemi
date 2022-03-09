def solution(tickets):
    dic = {}
    
    for i in tickets:
        dic[i[0]] = dic.get(i[0],[]) + [i[1]]
        
    #정렬
    for r in dic:
        dic[r].sort(reverse = True)
        
    #스택, 리스트 정의
    stk = ["ICN"]
    itinerary = []
    
    while len(stk) > 0:
        top = stk[-1]
        if top not in dic or len(dic[top]) == 0:
            itinerary.append(stk.pop())
        else:
            stk.append(dic[top].pop())
            
    return itinerary[::-1]