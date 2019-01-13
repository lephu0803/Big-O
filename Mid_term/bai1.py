n = int(input())


if n == 1:
    total = 1*15000
elif n>1 and n<6:
    total = 1*15000 + (n-1)*13500
elif n>=6:
    total = 1*15000 + 4*13500 + (n-5)*11000
    if n >=12:
        total = total - total*0.1

print(total)