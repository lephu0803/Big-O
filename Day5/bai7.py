n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
if n%2!=0:
    print('NO')
else:
    cnt = 0
    for i in a:
        if i==0:
            cnt+=1
        else:
            cnt-=1
    if cnt == 0:
        print('YES')
    else:
        print('NO')