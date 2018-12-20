def system_equal(a, b, n, m):
    if (a**2+b==n) and (a+b**2==m):
        return True 
    else: 
        return False

a = count = 0
# print(a,b,i,count)
n, m = map(int, input().split())
while (a**2<=n and a <=m):
    b = n-a**2
    if system_equal(a,b,n,m):
        count+=1
    a+=1

print(count)