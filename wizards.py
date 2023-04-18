def trapdoors(*data):
    a = {}
    for i in data:
        d = []
        if len(i) % 2 != 0:
            if i[len(i) // 2] in a:
                for j in a[i[len(i) // 2]]:
                    d.append(j)
            d.append(i)
            d = sorted(d)
            res = []
            for j in range(len(d) -1, -1, -1):
                res.append(d[j])
            a[i[len(i) // 2]] = res
    return a
data = [
    'bottles', 'cloak', 'darkness', 'cloud',
    'mountains', 'ray', 'rainbow'
]
print(trapdoors(*data))