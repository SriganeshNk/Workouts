from fractions import gcd

def read_num():
    s = long(raw_input())
    integer_pair = []
    while s != 0:
        pair = raw_input().split(' ')
        integer_pair.append((long(pair[0]), long(pair[1])))
        s -= 1
    return integer_pair

def find_max(numbers):
    numbers = sorted(numbers)
    x, y = numbers[0], numbers[1]
    if y%x == 0:
        return (y/x)-2
    else:
        common = gcd(y,x)
        return y/common - 2

def abs_unique():
    pair = read_num()
    answers = []
    for x,y in pair:
        if x == y:
            answers.append(0)
        else:
            answers.append(find_max([x, y]))
    for x in answers:
        print x

abs_unique()
