cases = long(raw_input())
result = []
while cases > 0:
    num = long(raw_input())
    n = num 
    i = 2
    while i * i < n:
        while n%i == 0:
            n = n / i
        i = i + 1
    if i*i == n:
        result.append(num/i)
    elif n == num:
        result.append(num/i)
    else:
        result.append(num/n)
    cases -= 1
for x in result:
    print x

"""students = 0
ids = 0
result = []
while cases > 0:
    ppl = int(raw_input())
    students = 0
    ids = 0
    while ppl > 0:
        spread = map(int,raw_input().split(' '))
        ids += spread[0]
        students += spread[1]
        ppl -= 1
    result.append(ids-students)
    cases -= 1
for x in result:
    print x
"""
