def anagrams(str1, str2):
    check = {}
    for x in str1:
        if x in check:
            check[x] += 1
        else:
            check[x] = 1
    for x in str2:
        if x in check:
            check[x] -= 1
        else:
            return False
    for x in check.values():
        if x != 0:
            return False
    return True

    
str1 = raw_input()
str2 = raw_input()
if anagrams(str1, str2):
    print "Anagrams!"
else:
    print "Not Anagrams!"
