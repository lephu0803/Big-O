
def doixung(x):
    x = str(x)
    # print(x[0])
    for i in range(int(len(x)/2)+1):
        if x[i] != x[len(x)-1-i]:
            return False
    return True

n = int(input())
if doixung(n):
    print('YES')
else:
    print('NO')
