n = int(input())
total = 0
maxx = 0
for i in range(n):
    a, b = map(int, input().split())
    total = total-a+b
    if total >= maxx:
        maxx = total
print(maxx)