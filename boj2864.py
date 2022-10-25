a, b = map(str, input().split())
maxa = maxb = mina = minb = ""

for i in range(len(a)):
    if a[i] != '5' and a[i] != 6:
        maxa += a[i]
        mina += a[i]
    else:
        maxa += '6'
        mina += '5'
maxa, mina = int(maxa), int(mina)
for i in range(len(b)):
    if b[i] != '5' and b[i] != '6':
        maxb += b[i]
        minb += b[i]
    else:
        maxb += '6'
        minb += '5'
maxb, minb = int(maxb), int(minb)
print("{} {}".format(mina + minb, maxa + maxb))