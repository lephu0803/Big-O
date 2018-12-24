n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
for i in a:
    if i%2==0:
        print(i)
        