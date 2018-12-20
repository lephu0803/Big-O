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
tong = 0
for i in range (2,n):
    if nguyento(i):
        tong +=i

print(tong)