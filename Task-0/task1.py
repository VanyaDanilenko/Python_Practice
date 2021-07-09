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

odd = []
for elt in arr:
    if elt % 2 != 0:
        odd.append(elt)
if len(odd) == 0:
    print('No numbers')
else:
    print('Odd:', sorted(odd, reverse=True))
