n = int(input())
cam = tao = 0 
idx = 0
for i in range(n):
    a, b = map(int, input().split(' '))
    if a >= tao:
        if b > cam:
            tao = a
            cam = b
            idx = i+1

print(idx)