def find_duplicate(ids, emp):
    emp_count = {}
    idx = 0
    count = 0
    while idx < ids:
        if emp[idx] not in emp_count:
            emp_count[emp[idx]] = 1
        else:
            emp_count[emp[idx]] += 1
        idx += 1
    for x in emp_count.values():
        if x > 1:
            count += 1
    return count


num = int(raw_input())
result = []
while num > 0:
    emp = []
    ids = int(raw_input().strip())
    dup = ids
    #emp = map(int,raw_input().strip().split(' '))
    while ids > 0:
        emp.append(int(raw_input().strip()))
        ids -= 1
    print emp
    result.append(find_duplicate(dup, emp))
    num -= 1
for x in result:
    print x
