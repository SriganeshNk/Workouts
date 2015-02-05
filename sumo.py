import collections
#line = map(int, raw_input().split(' '))
players, diff = 5,2 #line[0], line[1]
weights = [1,3,4,3,0] #map(int, raw_input().split(' '))
relate = collections.defaultdict(lambda: 0)
used = {}
result = []
num = 3 #int(raw_input())
line = [[0,1],[1,3],[0,4]]#map(int, raw_input().split(' '))\
k = 0
while num > 0:
    l, r = line[k][0], line[k][1]
    mass = sorted(weights[l:r+1])
    relate.clear()
    add_count = 0
    for y in range(l, r+1):
        if relate[weights[y]] > 0:
            add_count += 1
        relate[weights[y]] += 1
    count = 0
    used.clear()
    for x in range(len(mass)):
        for i in range(1, diff+1):
            if abs(mass[x]+i) in relate:
                count += relate[abs(mass[x]+i)]
            if abs(mass[x]-i) in relate and abs(mass[x]-i) != abs(mass[x]) and abs(mass[x]-i) != abs(mass[x]+i):
                count += relate[abs(mass[x]-i)]
        relate[mass[x]] -= 1
    result.append(count+add_count)
    k += 1
    num -= 1
for x in result:
    print x
