# Enter your code here. Read input from STDIN. Print output to STDOUT
def child (str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    n = len(str1)
    count = [[0 for x in range(n)]for y in range(n)]
    max_count = 0
    i, j, k = n-1, n-1, n-1
    while i >= 0:
        j = n-1
        while j >= 0:
            if str1[i] == str2[j]:
                if j == n-1 and i <= n-1:
                    count[i][j] = 1
                elif i < n-1 and j < n-1:
                    count[i][j] = 1+count[i+1][j]
                else:
                    count[i][j] = 1
            else:
                if j == n-1  and i <= n-1:
                    count[i][j] = 0
                elif i < n-1 and j < n-1:
                    count[i][j] = max(count[i][j+1], count[i+1][j])
                else:
                    count[i][j] = count[i][j+1]
            j -= 1
        i -= 1
    for x in count:
        print x
        max_count = max(max(x), max_count)
    return max_count

str1 = "OUDFRMYMAW"
str2 = "AWHYFCCMQX"
print child(str1, str2)
