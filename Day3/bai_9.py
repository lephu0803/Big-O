n = int(input())
height = 0
total = 0
# level = 1
while True:
    if (n-total)>=0:
        height +=1
        for i in range(height):
            total += (i+1)
        # height +=1
    else:
        break
print(height-1)