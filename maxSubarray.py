import bisect

def max_mod(array, M):
    L = [0] * (len(array) + 1)
    for i in range(1, len(L)):
        L[i] = L[i - 1] + array[i - 1]
    acc = 0
    done = []
    # print L
    for i in range(len(L)):
        x = L[i] % M
        j = bisect.bisect_right(done, x)
        print j
        acc = max(acc, x)
        # print done, (x, j), acc
        if j < i:
            acc = max(acc, (L[i] - done[j]) % M)
        done.insert(j, x)
    print done
    print L
    return acc
"""
for _ in range(input()):
    N, M = map(int, raw_input().split(" "))
    array = map(int, raw_input().split(" "))
    print max_mod(array, M)
"""
A = map(int, raw_input().split(' '))
print max_mod(A, 184803527)
