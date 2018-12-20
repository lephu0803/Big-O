def nguyento(a):
    if a < 2:
        return False
    elif(a==2):
        return True
    else:
        for i in range(2,int(a**0.5+1)):
            if (a%i == 0):
                return False

    return True

n = int(input())
x = 0
if nguyento(n):
    print(n)
else: 
    while True:
        x+=1
        if nguyento(n-x):
            print(n-x)
            break
        elif nguyento(n+x):
            print(n+x)
            break