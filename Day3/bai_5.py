x = 0
flag = True
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if n <= x:
            flag = False
        else:
            x = n

if flag == True:
    print('YES')
else:
    print('NO')
