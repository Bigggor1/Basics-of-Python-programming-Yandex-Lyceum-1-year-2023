def third_force(*rest, proof):
    a = {}
    one = []
    two = []
    three = []
    for i in rest:
        if proof in i:
            one.append(i)
        if (proof.lower() in i and proof.isupper()) or (proof.upper() in i and proof.islower()):
            three.append(i)
        elif proof.lower() not in i and proof.upper() not in i:
            two.append(i)
    a['1'] = sorted(one)
    a['2'] = sorted(two)
    a['3'] = sorted(three)
    return a