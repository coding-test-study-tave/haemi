def number_finder(N):
    for i in range(1, 2**100):
        bin_num = int(bin(i)[2:])
        if not bin_num%N:
            return bin_num
    return 'BRAK'

T = int(input())
N_list = []
for _ in range(T):
    N = int(input())
    N_list.append(N)
    
for N in N_list:
    print(number_finder(N))