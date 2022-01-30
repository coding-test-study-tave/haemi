heights = []
for _ in range(9):
    heights.append(int(input()))
heights = sorted(heights)

def check_true_dwarfs(heights):
    for i in range(8):
        for j in range(i+1, 9):
            h_sum = sum(heights)
            true_sum = h_sum - heights[i] - heights[j]
            if true_sum == 100:
                heights.pop(j)
                heights.pop(i)
                return heights
            else: continue
    return 0

check = check_true_dwarfs(heights)
for elem in check:
    print(elem)
