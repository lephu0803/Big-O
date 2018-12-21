n = int(input())
a = list(map(int,input().split(' ')))
# minn = 100000000000
minn = 0
for i in range(n-1,0,-1):
    if a[i] < a[i-1]:
        tmp = a[i-1]
        a[i-1] = a[i]
        a[i] = tmp

for j in range(n-1):
    for i in range(n-1,j,-1):
        if a[i] < a[i-1]:
            tmp = a[i-1]
            a[i-1] = a[i]
            a[i] = tmp
    if (a[j+1] - a[j]) >1:
        minn = a[j]+1
        print(minn)
        break
if minn==0:
    print(a[-1]+1)
# minn = 100000
# for i in range(n):
#     if (a[i+1]-a[i]) > 1:
#         print(a[i]+1)
#         break


