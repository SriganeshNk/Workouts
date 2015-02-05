def isInterleave(s1, s2, s3):
        if len(s1) == len(s2) == 0 and len(s3) == 0:
            return True
        if len(s1) + len(s2) > len(s3):
            return False
        IL = []
        for i in range(len(s1)+1):
            L = []
            for j in range(len(s2)+1):
                L.append(False)
            IL.append(L)
        i, j, x = 0, 0, 0
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    IL[i][j] = True
                #A is empty
                elif i==0 and s2[j-1] ==s3[j-1]:
                    IL[i][j] = IL[i][j-1]
     
                #B is empty
                elif j==0 and s1[i-1]==s3[i-1]:
                    IL[i][j] = IL[i-1][j]
     
                # Current character of C matches with current character of A,
                # but doesn't match with current character of B
                elif check(i,j) and s1[i-1]==s3[i+j-1] and s2[j-1]!=s3[i+j-1]:
                    IL[i][j] = IL[i-1][j]
     
                # Current character of C matches with current character of B,
                # but doesn't match with current character of A
                elif check(i,j) and s1[i-1]!=s3[i+j-1] and s2[j-1]==s3[i+j-1]:
                    IL[i][j] = IL[i][j-1]
            
                # Current character of C matches with that of both A and B
                elif check(i,j) and s1[i-1]==s3[i+j-1] and s2[j-1]==s3[i+j-1]:
                    IL[i][j]= IL[i-1][j] or IL[i][j-1]
        return IL[len(s1)][len(s2)]

def check(i,j):
    if i-1 >= 0 and j-1 >= 0:
        return True

if isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"):
#if isInterleave("a","", "c"):
    print True
else:
    print False
