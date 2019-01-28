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

if __name__ == "__main__":
    m, n, k = map(int,input().split())
    a = list( map(int, input().split()) )
    b = list(map(int,input().split()))
    c = merge(a,b, reverse=True)
    print(c[-(k+1)])
