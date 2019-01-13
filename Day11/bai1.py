def insertionSort(a):
    for i in range(0,len(a)):
        x = a[i]
        for j in range(i,0,-1):
            if (a[j-1] > x) and(j>0):
                a[j] = a[j-1]
                a[j-1] = x
    return a

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a = insertionSort(a)
    for i in a:
        print(i, end=' ')
