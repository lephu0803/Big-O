n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
tong = 0 
for i in a:
    tong+=i
print(tong)