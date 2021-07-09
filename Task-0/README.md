# Task Completion Details Task-0 

<br>
<h2 align="center">Connection ssh</h2>

### Example commands

```shell
$ ssh-keygen -t rsa -b 4096 -C "email@"
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
```
<kbd>
    <img src="../Images/Screenshot-3.png" width="700px" title="Connection ssh">
</kbd>
    
<br>
<br>
<hr>

<h2 align="center">Task-0</h2>
<p align="left">Option 1: 1-Form a list of 30 different whole numbers from -100 to + 100. Know the maximum element in the list і th ordinal number. Rewrite the list to add only unpaired numbers on the list, or perhaps, there are no such numbers. Otrimaniy list to put in order the change of elements.</p>

### Example

```python
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
```

<em><p align="left">Screenshots of program execution are shown below:</p></em>

<kbd>
    <img src="../Images/Screenshot-1_Task-1.png" width="700px" title="Task-0">
</kbd>
 
<br>
<br>

<p align="left">Option 2: 2-Form a list of 30 different numbers from -100 to + 100. To know the maximum element in the list and the first ordinal number. To bet on all numbers, to stand the order.</p>

### Example

```python
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

res = []
for i in couples(arr):
    pr = []
    if i[0] == '-':
        for _ in range(i[2][1]-i[2][0]+1):
            pr.append(i[1])
        res.append(pr)

print('Couple:', None if len(res) == 0 else res)
```

<br>
<em><p align="left">Screenshots of program execution are shown below:</p></em>

<kbd>
    <img src="../Images/Screenshot-2_Task-2.png" width="700px" alt="Task-1">
</kbd>
