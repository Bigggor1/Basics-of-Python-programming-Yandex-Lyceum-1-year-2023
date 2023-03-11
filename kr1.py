from random import randrange, choice


b = input().split()
c = input().split()
v = input().split()
for i in range(3):
    product = choice(b)
    b.remove(product)
    weight = randrange(round(float(v[0]), 1) * 10, round(float(v[1]), 1) * 10) / 10
    value = randrange(int(c[0]), int(c[1]))
    total = value * weight
    print(f'{i + 1}. {product} weighing {weight} kg, {value} of pieces, {round(total, 1)} kg.')