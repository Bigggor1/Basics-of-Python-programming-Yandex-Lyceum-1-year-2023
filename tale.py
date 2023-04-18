import sys


data = []
for line in sys.stdin:
    data.append(line.rstrip('\n'))

lst = []
for i in data:
    i = i.split()
    a = []
    for j in range(len(i)):
        if j % 2 == 0:
            a.append(i[j])
    lst.append((a))
result = sorted(lst, key=len)
for i in result:
    print(' '.join(i))