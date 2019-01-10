def count(a):
    cnt = 0
    for i in range(0, (len(a) - 1)):
        if a[i] != a[i+1]:
            cnt += 1
    return cnt+1

n = int(input())
a = []
for i in range(n):
    x = str(input())
    a.append(x)

print(count(a))