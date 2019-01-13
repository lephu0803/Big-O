def merge(L,R):
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

def mergeSort(a):
    if len(a)<=1:
        return(a)
    else:
        k = len(a)//2
        L = a[:k]
        R = a[k:]
        b = merge(mergeSort(L),mergeSort(R))
    return b

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    x = mergeSort(a)
    for i in x:
        print(i, end=' ')
