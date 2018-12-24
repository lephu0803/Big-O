n = int(input())
raw_in = input().split(' ')
a = [int(num) for num in raw_in]
def kiemtra(a):
    for i in a:
        if i==0:
            return False
    return True

if kiemtra(a):
    print('YES')
else: 
    print('NO')