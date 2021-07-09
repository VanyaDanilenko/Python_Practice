import random
arr = []

for _ in range(0, 30):
    arr.append(random.randint(-100, 100))

print('Array:', arr)
print('Max:', max(arr))

clist = 1
for index, i in enumerate(arr):
    if i == max(arr):
        print('   %s) Index (%s) = %s' % (clist, index, i))
        clist+=1

def couples(scr):
    res = []

    variable = 0
    number = 0
    pos = [-1, -1]
    for index, i in enumerate(scr):
        if index == 0:
            variable = i
            pos[0] = index
        else:
            if i == variable:
                number = i
                pos[1] = index
            else:
                if pos[1] - pos[0] > 0:
                    res.append(['+' if number >= 0 else '-', number, [pos[0], pos[1]]])
                variable = i
                pos[0] = index
    return res

# print(couples(arr))

res = []
for i in couples(arr):
    pr = []
    if i[0] == '-':
        for _ in range(i[2][1]-i[2][0]+1):
            pr.append(i[1])
        res.append(pr)

print('Couple:', None if len(res) == 0 else res)
