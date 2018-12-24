m, n = map(int,input().split())
x = []
s = ''
for i in range(m):
    a = list(map(int,input().split(' ')))
    x.append(a)
cnt = 0
def nguyento(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if (x%i==0) and not (x==i):
                return False
    return True

for i in range(m):
    if i == 0 or i==m-1:
        for j in range(n):
            if nguyento(x[i][j]):
                cnt+=1
    else: 
        if nguyento(x[i][0]):
            cnt+=1
        if nguyento(x[i][n-1]):
            cnt+=1
print(cnt)