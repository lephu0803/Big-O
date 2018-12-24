def nguyento(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if (x%i==0) and not (x==i):
                return False
    return True

n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
cnt = 0
for i in a:
    if nguyento(i):
        cnt+=1
print(cnt)
# print(nguyento(2))