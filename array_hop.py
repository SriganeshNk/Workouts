import sys
def  array_hop(a):
    jumps = [sys.maxint for x in a]
    jumps.append(sys.maxint)
    jumps[0] = 0
    path = [0 for x in a]
    path.append(sys.maxint)
    pathstr = ''
    n = len(a)
    if n > 0 and a[0] == 0:
        return ""
    if n == 0:
        return ""
    i, j = 1, 0
    while i <= n:
        j = 0
        while j < n:
            if i <= a[j] + j and jumps[j] != sys.maxint:
                jumps[i] = min(jumps[i], jumps[j]+1)
                path[i] = j
                break
            j += 1
        i += 1
    x = path[n]
    print jumps
    print path
    while x > 0:
        pathstr = str(x) + ', ' + pathstr
        x = path[x]
    if len(pathstr) == 0:
        print failure
        return
    print '0, ' + pathstr + 'out'
    

a = [5,6,0,4,2,4,1,0,0,4]
print a
array_hop(a)
