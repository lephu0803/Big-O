m,n = map(int,input().split())
a = []
Mat = []
for i in range(m):
    x = list(map(int,input().split()))
    mat = [1]
    maxx = x[0]
    tmp_id = 0
    for j in range(1,n):
        if x[j]>maxx:
            maxx = x[j]
            mat.append(1)
            mat[tmp_id] = 0
            tmp_id = j
        elif: 
            
        else:
            mat.append(0)
    Mat.append(mat)
    a.append(x)
for i in range(m):
    for j in range(n):
        if Mat[i] == 1:
            

