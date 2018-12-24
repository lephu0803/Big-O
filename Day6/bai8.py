n = int(input())
m = n
a = []
Matx = []
for i in range(m):
    x = list(map(int,input().split()))
    mat = []
    maxx = x[0]
    tmp_id = 0
    for j in range(1,n):
        if x[j] > maxx:
            maxx = x[j]
    for j in range(n):
        if x[j] == maxx:
            mat.append(1)
        else:
            mat.append(0)
    # print(mat)
    Matx.append(mat)
    a.append(x)

Maty = [[0 for y in range(n)] for x in range(m)]
for j in range(n):
    maxx = a[0][j]
    for i in range(1,m):
        if a[i][j] > maxx:
            maxx = a[i][j]
    for i in range(m):
        if a[i][j] == maxx:
            Maty[i][j] = 1
Matcp = [[1 for y in range(n)] for x in range(m)]
# for i in range(m):
#     for j in range(n):
#         if (Matx[i][j] == 1) and (Maty==1):
#             for j in range (n):
#                 tmp_max = a[0][j]
#                 for k in range(m):  
for i in range(1,m):
    maxx = a[i][0]
    for k in range(0,i+1):
        if a[i-k][k] > maxx:
            maxx=a[i-k][k]
    # print(maxx)
    for k in range(0,i+1):
        # print('max', maxx)
        # print(a[i-k][k])
        if a[i-k][k] < maxx:
            Matcp[i-k][k]=0
        
for j in range(1,n):
    h = m-1
    maxx = a[m-1][j]
    for k in range(j,n):
        if a[h][k] > maxx:
            maxx = a[h][k]
        h=h-1
    h = m-1
    for k in range(j,n):
        if a[h][k] < maxx:
            Matcp[h][k] = 0
        h=h-1
for j in reversed(range(n)):
    h = 0
    maxx = a[0][j]
    for k in range(j,n):
        if a[h][k] > maxx:
            maxx = a[h][k]
        h+=1
    h = 0
    for k in range(j,n):
        if a[h][k] < maxx:
            Matcp[h][k] = 0
        h+=1
for i in range(1,m):
    maxx=a[i][0]
    for k in range(n-i):
        if a[i][k] > maxx:
            maxx = a[i][k]
    for k in range(n-i):
        # print(maxx)
        if a[i][k] < maxx:
            Matcp[i][k] = 0
print(Matcp)
cnt=0 
for i in range(m):
    for j in range(n):
        if Matx[i][j]==1 and Maty[i][j]==1 and Matcp[i][j]==1:
            cnt+=1
print(Matx)
print(Maty)
# print(cnt)
# print(Matcp)
# for i in range()
