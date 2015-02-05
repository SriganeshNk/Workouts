# Enter your code here. Read input from STDIN. Print output to STDOUT
def partition(a):
    n = len(a)
    last = n-2
    first = 0
    pivot = n-1
    while first < last:
        while a[last] > a[pivot] and last >= 0:
            last -= 1
        while a[first] < a[pivot] and first < pivot:
            first += 1
        if first < last and last >= 0:
            a[first], a[last] = a[last], a[first]
            first += 1
            last -= 1
    if first < pivot:
        a[first], a[pivot] = a[pivot], a[first]
    return (first, a)

def find_median(arr):
    if len(arr) == 0:
        return 
    if len(arr) == 1:
        print arr[1]
        return
    if len(arr) == 2:
        print (arr[0]+arr[1])/2
        return
    x = len(arr)+1
    n = len(arr)
    while x != n/2:
        x, arr = partition(arr[:x])
    print arr[x]
    return

arr = map(int, raw_input().split(' '))
print arr[1]
find_median(arr)
