import math 
n = int(input())
flag = True
if (n == 0) or (n==1):
    flag = False
elif (n==2):
    flag = True
else:
    for i in range(int(n**0.5)+1):
        # print(n%(i+2))
        if (n%(i+2) == 0):
            if i+2 != n:

                flag = False
        
if flag == True:
    print('YES')
elif flag == False:
    print('NO')
    