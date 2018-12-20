def max(a):
    a = str(a)
    maxx = 0
    for i in a:
        # print(i)
        if int(i) > maxx:
            maxx = int(i) 
    return maxx

n = int(input())
print(max(n))