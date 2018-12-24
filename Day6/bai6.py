m, n = map(int,input().split())
# m = int(input())
a = []
# s = ''
for i in range(m):
    x = list(map(int,input().split(' ')))
    a.append(x)
maxx = 1
for i in range(m):
    cnt=0
    for j in range(n):
        if a[i][j]%2==0:
            cnt+=1
    if cnt == n:
        kq = i
        break
    if cnt > maxx:
        kq = i
        maxx = cnt
print(kq)