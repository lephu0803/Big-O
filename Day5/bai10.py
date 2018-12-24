n = int(input())
a = list(map(int,input().split(' ')))
flag=True
cnt = 0
for i in a:
    if i == 0:
        cnt +=