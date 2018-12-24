m,n = map(int,input().split())
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
    minn = a[0][j]
    for i in range(1,m):
        if a[i][j] < minn:
            minn = a[i][j]
    for i in range(m):
        if a[i][j] == minn:
            Maty[i][j] = 1
# print(Maty)
count = 0
for i in range(m):
    for j in range(n):
        if (Matx[i][j] == 1) and (Maty[i][j]==1):
            count+=1

print(count)


            

