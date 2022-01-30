def bin_number_generator(length):
    if length==1:
        return ['0','1']
    else:
        before = bin_number_generator(length-1)
        present = ['0'+num for num in before] + ['1'+num for num in before]
        return present

def full_bin_number_generator(length):
    if length==1:
        return ['1']
    else:
        return ['1'+num for num in bin_number_generator(length-1)]

def number_finder(denom):
    length = 1
    while length <= 100:
        num_list = full_bin_number_generator(length)
        for num in num_list:
            if not int(num)%denom:
                return int(num)
        length += 1
    return('BRAK')

T = int(input())
N_list = []
for _ in range(T):
    N = int(input())
    N_list.append(N)
    
for N in N_list:
    print(number_finder(N))
        