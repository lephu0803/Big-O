n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
maxx = 0
for i in a:
    if i>maxx:
        maxx=i
print(maxx)