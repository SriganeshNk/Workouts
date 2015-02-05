def isPresent(seq, dictionary):
    if len(seq) == 0:
        return True
    word = ''
    for x in range(len(seq)):
        word += seq[x]
        if word in dictionary:
            if isPresent(seq[x+1:], dictionary):
                return True
    return False

d = {'remote': 1, 'rem':1, 'tv': 1, 'able': 1, 'channel': 1, 'hello': 1, 'hi': 1, 'hic': 1}
seq = ['remotehicable', 'hellocablexyz', 'hellohicable', 'remremote']
for x in seq:
    print isPresent(x, d)

f = open('bloom_word.py', 'r')
for line in f:
    print line
