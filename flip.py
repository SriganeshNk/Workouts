import ctypes
def flip_bits(num):
    i = 0
    result = num
    while i < 32:
        result ^= (1 << i)
        i += 1
    print result
    return result

def max_xor(upper, lower):
    temp = upper
    l = lower
    result = 0
    while upper > lower:
        temp = upper ^ lower 
        if result < temp:
            result = temp
        lower += 1
    lower = l
    while upper > lower:
        temp = upper ^ lower 
        if result < temp:
            result = temp
        upper -= 1
    return result


print max_xor(7, 5)
"""
num = int(raw_input())
while num > 0:
    i = int(raw_input())
    print flip_bits(i)
    num -= 1
"""
