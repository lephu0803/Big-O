minn = 10
maxx = 0
while True:
    n = int(input())
    if n == -1:
        print('{} {}'.format(maxx,minn))
        break
    else:
        if n <= minn:
            minn = n
        if n >= maxx:
            maxx = n 
