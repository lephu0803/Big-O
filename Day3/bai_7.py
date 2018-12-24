n = int(input())
fence = '*'
white = ' '
for i in range(n):
    if i == 0:
        print(fence*n)
    elif i == (n-1):
        print(fence*n)
    else:
        print('*{}*'.format(white*(n-2)))
        