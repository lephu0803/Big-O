def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if (x%i==0) and not (x==i):
                return False
    return True

def insertionSort(a, reverse=False):
    if not reverse:
        for i in range(1,len(a)):
            x = a[i]
            for j in range(i,0,-1):
                if (a[j-1] > x) and(j>0):
                    a[j] = a[j-1]
                    a[j-1] = x
    else: 
        for i in range(1,len(a)):
            x = a[i]
            for j in range(i,0,-1):
                if (a[j-1] < x) and(j>0):
                    a[j] = a[j-1]
                    a[j-1] = x
    return a

if __name__ == "__main__":
    # n = 5
    # a = [4,6,3,1,2]
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in a:
        if not isPrime(i):
            b.append(i) 
    b = insertionSort(b)
    j = 0
    for i in range(len(a)):
        if not isPrime(a[i]):
            print(b[j], end=' ')
            j += 1
        else:
            print(a[i], end =' ')