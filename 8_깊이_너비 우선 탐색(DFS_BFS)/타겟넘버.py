def solution(numbers, target):
    tree = [0] #처음 트리의 층수는 0
    for sub_num in numbers: #숫자 배열에서 하나씩 숫자 꺼내중
        sub_tree = []
        for tree_num in tree: #자식노드 생성
            sub_tree.append(tree_num + sub_num)
            sub_tree.append(tree_num - sub_num)
        tree = sub_tree
    return tree.count(target)

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

#나올수있는 모든 경우의 수들을 leaves에 넣어 놓고, 
#그 중 답에 해당하는 것과 같은것의 수를 출력