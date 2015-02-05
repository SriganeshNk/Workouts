def fractionToDecimal(numerator, denominator):
        ans = float(numerator)/float(denominator)
        string = str(ans)
        print string
        final = []
        repeat = False
        for i in range(len(string)-1):
            temp = string[i]
            if temp == string[i+1] and not repeat:
                final.append('(')
                final.append(temp)
                repeat = True
            else:
                if repeat and temp != string[i+1]:
                    final.append(')')
                    repeat = False
                final.append(temp)
        final.append(string[len(string)-1])
        string = ''.join(map(str, final))
        print string

fractionToDecimal(1, 5)
