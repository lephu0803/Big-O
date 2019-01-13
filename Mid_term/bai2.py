n = int(input())
for i in range(n):
    space = ' '
    star = '*'
    star = star*(2*i+1)
    space = space*int(((2*n-1)-(2*i+1))/2)
    print(space+star+space)
