N, M = map(int, input().split())
order_dict = dict()

for n in range(1, N+1):
    order_dict[n] = [[],[]] # front, behind

# {1 : [[2, 3, 4, 5, 6], []], 2 : [[3, 4, 5, 6], [1]], ... }

for _ in range(M):
    front, behind = map(int, input().split())
    order_dict[front][1].append(behind)
    order_dict[behind][0].append(front)

# order_dict : 모든 n에 대해 대소관계를 비교해 놓은 dict... 메모리 문제 발생할수도

def upgoing(tree, child_index):
    parent_index = (child_index-1)//2
    parent, child = tree[parent_index], tree[child_index]
    if child in order_dict[parent][1]:
        return tree
    elif not (child in order_dict[parent][1]):
        tree[parent_index], tree[child_index] = child, parent
        upgoing(tree, parent_index)






# bin_tree = []
# for front, behind in order_pair_list:
#     if not bin_tree:
#         bin_tree.append(front)
#         bin_tree.append(behind)

#     else:
#         front_exists = front in bin_tree
#         behind_exists = behind in bin_tree
#         if front_exists & behind_exists:
#             front_index = bin_tree.index(front)
#             behind_index = bin_tree.index(behind)
#             if front_index < behind_index:
#                 pass
#             else:

