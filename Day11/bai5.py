def merge(L,R,reverse=False):
    if not reverse:
        inf=10000001
        a = []
        L.append(inf)
        R.append(inf)
        i = j = 0
        while (i<len(L)-1) or (j<len(R)-1):
            if L[i] < R[j]:
                a.append(L[i])
                i+=1
            else:
                a.append(R[j])
                j+=1
    else:
        inf=-10000001
        a = []
        L.append(inf)
        R.append(inf)
        i = j = 0
        while (i<len(L)-1) or (j<len(R)-1):
            if L[i] > R[j]:
                a.append(L[i])
                i+=1
            else:
                a.append(R[j])
                j+=1
    return a

def mergeSort(a, reverse=False):
    if len(a)<=1:
        return(a)
    else:
        k = len(a)//2
        L = a[:k]
        R = a[k:]
    return merge(mergeSort(L, reverse=reverse),mergeSort(R, reverse=reverse), reverse=reverse)

if __name__ == "__main__":
    n = int(input())
    a=list(map(int,input().split()))
    # n = 5
    # a=[4,6,1,2,3]
    odd = []
    even = []
    for i in a:
        if i%2==0:
            even.append(i) 
        else:
            odd.append(i)
    even=mergeSort(even)
    odd=mergeSort(odd,reverse=True)
    k=t=0
    for i in range(n):
        if a[i]%2==0:
            print(even[k], end=' ')
            k+=1
        else:
            print(odd[t],end=' ')
            t+=1
