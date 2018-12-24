m, n = map(int,input().split())
a, b, p = map(int,input().split())
matrix = []
x = []
for j in range(n):
    if j == 0:
        x.append(a)
    elif j==1:
        x.append(b)
    else:
        x.append((x[j-1]+x[j-2])%p)
matrix.append(x)
# print(matrix[0][1])
for i in range(1,m):
    x = []
    for j in range(n):
        if j==0:
            x.append((matrix[i-1][n-1]+matrix[i-1][n-2])%p)
            # print(x)
        elif j==1: 
            x.append((matrix[i-1][n-1]+x[j-1])%p)
        else:
            x.append((x[j-1]+x[j-2])%p)
    matrix.append(x)
for tmp in matrix:
    for j in tmp:
        print(j,end=' ')
    print()