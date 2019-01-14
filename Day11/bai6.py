class Student(object):
    def __init__(self,idx=0,point=0):
        self.idx=int(idx)
        self.point=point
    def __getattribute__(self,name):
        return object.__getattribute__(self,name)

def merge(L,R,reverse=False,key=None):    

    if not reverse:
        inf=10000001
        a = []
        L.append(inf)
        R.append(inf)
        i = j = 0
        while (i<len(L)-1) or (j<len(R)-1):
            if key==None:
                if L[i] < R[j]:
                    a.append(L[i])
                    i+=1
                else:
                    a.append(R[j])
                    j+=1
            else:
                if key(L[i]) < key(R[j]):
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
            if key==None:
                if L[i] > R[j]:
                    a.append(L[i])
                    i+=1
                else:
                    a.append(R[j])
                    j+=1
            else:
                if key(L[i]) > key(R[j]):
                    a.append(L[i])
                    i+=1
                else:
                    a.append(R[j])
                    j+=1

    return a

def mergeSort(a, reverse=False, key=None):
    if len(a)<=1:
        return(a)
    else:
        k = len(a)//2
        L = a[:k]
        R = a[k:]
    return merge(mergeSort(L, reverse=reverse, key=key),mergeSort(R, reverse=reverse, key=key), reverse=reverse,key=key)

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        idx,point=map(float,input().split())
        a.append(Student(idx,point))
    a = mergeSort(a, reverse=True, key=lambda x: x.point)
    for i in range(k):
        print(a[i])
