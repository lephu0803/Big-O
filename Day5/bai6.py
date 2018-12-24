n = int(input())
a = list(map(int,input().split(' ')))
minn = a[0]
energy = 0
for i in a:
    if i<minn:
        minn = i
for i in a:
    if i > minn:
        energy+= (i-minn)
print(energy)