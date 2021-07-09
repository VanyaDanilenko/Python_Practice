# Examples line:
# the literal 1e-4 is interpreted as 10 raised to the power -4, which is 1/100, or 0.01.
# if writing int(5.0 / 2) seems a little long winded to you
# what do you think 0.1 + 0.2 is? The answer is 0.3, right?

import random

print('\033[33;1mPlease enter your string:\033[0m ', end='')
line = input()

newline = ''
numarr = []

for index, i in enumerate(line):
    if i >= '0' and i <= '9':
        numarr.append([int(i), int(index)])

for i in line:
    if i >= '0' and i <= '9':
        continue
    else:
        newline += i

print('\n\033[32;1mString without numbers:\033[0m', newline)
print('\033[32;1mString of numbers:\033[0m ', numarr)

words = []
words = line.split()

for index, i in enumerate(words):
    words[index] = words[index][0].upper() + words[index][1:-1] + words[index][-1].upper()
print('\033[32;1mWith a capital letter:\033[0m ', ' '.join(words), '\n')

maxn = -1
for i in numarr:
    if int(i[0]) > maxn:
        maxn = int(i[0])

degreearr = []
for i in numarr:
    if int(i[0]) != maxn:
        degreearr.append([i[0], i[0]**i[1], i[1]])

print('\033[33mMax int in array: ' + str(maxn) + '\033[0m')
print('\033[32;1mRaising numbers to powers by their index ( \033[0m\033[33;1m[number, exponentiation, index], ...\033[0m\033[32;1m ):\033[0m', degreearr)
print('----------   Done!   ----------')
