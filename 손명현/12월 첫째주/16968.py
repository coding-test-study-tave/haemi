car_id = list(input())

def number(unit):
    if unit=='c' : num = 26
    else         : num = 10
    return num

res = 1
first = car_id[0]

if first == 'c' : 
    prev = 'd'
else            : 
    prev = 'c'

for unit in car_id:
    if prev == unit:
        res*=(number(unit)-1)
    else:
        res*=number(unit)
    prev = unit

print(res)