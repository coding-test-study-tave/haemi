N = int(input())
district = []
for _ in range(N):
    district.append(list(map(int, input().split())))

def check_dist(r, c, x, y, d1, d2):
    if (r < x+d1) & (c <= y) & (r < -c+y+x) : return 1
    elif (r <= x+d2) & (c > y) & (r < c-y+x) : return 2
    elif (r >= x+d1) & (c < y+d2-d1) & (r > c+x-y+2*d1) : return 3
    elif (r > x+d2) & (c >= y+d2-d1) & (r > -c+y+x+2*d2) : return 4
    else : return 5

def get_max_min_diff(x, y, d1, d2):
    pop_list = [0, 0, 0, 0, 0]
    for r in range(1, N+1):
        for c in range(1, N+1):
            dist_num = check_dist(r, c, x, y, d1, d2)
            pop_list[dist_num-1] += district[r-1][c-1]
            
    res = max(pop_list) - min(pop_list)
    return res

min_overall = 0
for d1d2 in range(2, N):
    for d1 in range(1, d1d2):
        d2 = d1d2-d1
        for x in range(1, N-d1-d2+1):
            for y in range(d1+1, N-d2+1):
                new_val = get_max_min_diff(x, y, d1, d2)
                if not min_overall:
                    min_overall = new_val
                else:
                    if min_overall > new_val:
                        min_overall = new_val
print(min_overall)