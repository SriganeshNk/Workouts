line = raw_input().split()
per, sub = int(line[0]), int(line[1])
plot = []
while per > 0:
    plot.append(raw_input())
    per -= 1
i, j = 0, 0
max_sub = 0
teams = 0
while i < len(plot)-1:
    temp = int(plot[i], 2)
    k = i + 1
    while k < len(plot):
        temp1 = int(plot[k], 2)
        temp2 = temp1 | temp
        new_sub = bin(temp2).count("1")
        if new_sub == max_sub:
            teams += 1
        if new_sub > max_sub:
            teams = 1
            max_sub = new_sub
        k += 1
    i += 1
print max_sub
print teams
