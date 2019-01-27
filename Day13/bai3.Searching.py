def search(a, x, left, right):
    if left > right:
        return -1
    else:
        tmp = (left + right)//2
        if a[tmp]==x:
            return tmp+1
        elif a[tmp]>x:
            return search(a,x,left,tmp-1)       
        else:
            return search(a,x,tmp+1,right)
        
    

n, k = map(int,input().split())
a = list(map(int,input().split()))
print(search(a,k,0,n))