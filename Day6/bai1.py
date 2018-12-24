m, n = map(int,input().split())
x = []
for i in range(m):
    a = list(map(int,input().split(' ')))
    x.append(a)

for i in range(m):
    tong = 0
    for j in range(n):
        tong += int(x[i][j])
    print('{}: {}'.format(i,tong))