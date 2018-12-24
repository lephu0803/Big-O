m, n = map(int,input().split())
# m = int(input())
a = []
for i in range(m):
    x = list(map(int,input().split(' ')))
    a.append(x)
cnt=0
for i in range(m):
    for j in range(n):
        if a[i][j] > 100:
            cnt+=1
print(cnt)