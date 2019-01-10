n = int(input())
if n < 2:
    total = 15000
elif n >= 2 and n <= 5:
    total = 15000 + (n-1)*13500
else:
    if n < 12:
        total = 15000 + 13500*4 + (n-5)*11000
    else:
        total = int(0.9*(15000 + 13500*4 + (n-5)*11000))

print(total)