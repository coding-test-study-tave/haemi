N, K = map(int, input().split())

path_list = [[N, K, 0, 0]]

while True:
    n, k, p, s = path_list[0][0], path_list[0][1], path_list[0][2], path_list[0][3] # past, second
    print(n, k, p, s)
    if n == k:
        break
    elif n >= 1:
        if n < k:
            path_list.append([n-1, k, n, s+1])
            path_list.append([n+1, k, n, s+1])
            path_list.append([2*n, k, n, s+1]) 
        else :
            path_list.append([n-1, k, n, s+1])
    elif n == 0:
        path_list.append([n+1, k, n, s+1])
    elif n < 0:
        path_list.pop(0)
        continue
    path_list.pop(0)

print(s)