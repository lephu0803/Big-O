def gcd(a,b):
    if (a==0 or b ==0):
        return a+b
    elif a == b:
        return a
    while (a*b !=0):
        if a > b:
            a%=b
        else:
            b%=a
    return a+b 

a, b = map(int, input().split())

uc = gcd(a,b)
print(int(a/uc), int((b/uc)))