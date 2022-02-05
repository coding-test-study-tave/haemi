from collections import Counter

def solution(clothes): #counter 함수 이용
    # Key: 종류, Value: 개수로 Dictionary 만들기 
    count = Counter([kind for name, kind in clothes])
    
    # 곱집합 개수 구하기
    cases = 1
    for v in count.values():
        cases *= v + 1
    return cases - 1 #(A+1) * (B+1) - 1