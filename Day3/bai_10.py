def lucky(x):
    x = str(x)
    for i in x:
        if i != '7'and i != '4':
            return False
    return True

n = int(input())
if lucky(n):
    print('YES')
else:
    for i in range(int(n**0.5)+1):
        # print(i+1)
        # print(n/(i+1))
        if n%(i+1)==0 and (lucky(i+1) or lucky(int(n/(i+1)))):
            print('YES')
            break
        elif i == int(n**0.5):
            print('NO')
    