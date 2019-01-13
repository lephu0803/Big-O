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
    n=int(input())
    a=list(map(int,input().split()))
    # n = 6
    # a = [9,7,3,1,2,4]
    a = mergeSort(a)
    if n%2==0:
        print((a[n//2-1]+a[n//2])/2)
    else:
        print(a[n//2])
        