m = int(input())
x = []
s = ''
for i in range(m):
    a = list(map(int,input().split(' ')))
    x.append(a)
cnt = 1
flag =False
def nguyento(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if (x%i==0) and not (x==i):
                return False
    return True

for i in range(m):
    if nguyento(x[i][m-1-i]):
        flag = True
        cnt= cnt*x[i][m-1-i]
if flag==True:
    print(cnt%1000003)
else:
    print('1')