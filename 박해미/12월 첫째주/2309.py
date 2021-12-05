#큰거 두개 찾아서 빼기 => 9C2 = 9*8/2*1 = 36
#난쟁이가 N명이면 시간복잡도는 N^2

import sys
n=9
a=[int(input()) for _ in range (n)]
a.sort()
total=sum(a)
for i in range (0, n):
    for j in range(i+1, n):
        if total-a[i]-a[j] == 100:
            for k in range(0,n):
                if i == k or j == k: 
                    continue
                print(a[k])
            sys.exit(0)
