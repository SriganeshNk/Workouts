def rev_diagonal(x):
    n = len(x)
    result = []
    i = 2*n-2
    while i >= 0:
        temp = []
        z = i-n+1 if i >= n else 0
        j = z
        while j <= i - z:
            temp.append(x[j][i - j])
            j += 1
        result.append(temp)
        i-=1
    print result

x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
rev_diagonal(x)
