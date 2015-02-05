def read_num():
    s = long(raw_input())
    integer_pair = []
    while s != 0:
        number = long(raw_input())
        integer_pair.append(number)
        s -= 1
    return integer_pair
 
def abs_unique():
    pair = read_num()
    answers = []
    for x in pair:
        val = x%3
        num = x/3
        if val == 0:
            print pow(3,num,1000000007)
        if val == 1:
            print pow(3,(num-1),1000000007)*4%1000000007
        if val == 2:
            print 2*pow(3,num,1000000007)%1000000007
 
abs_unique() 
