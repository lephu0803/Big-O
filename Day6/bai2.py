m, n = map(int,input().split())
x = []
s = ''
for i in range(m):
    a = list(map(int,input().split(' ')))
    x.append(a)
for j in range(n):
    for i in range(m):
        if x[i][j] >= 0:
            break
        elif i==(m-1):
            s=s+str(j)+' '
print(s)