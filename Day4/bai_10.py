a = int(input())
b = int(input())
c = a+b
def kiemtra(x):
    x = str(x)
    for i in x:
        # print(i)
        if i == '0':
            return True
    return False

def xoaso(x):
    ketqua = ''
    x = str(x)
    for i in x:
        if i != '0':
            ketqua += i

    return int(ketqua)

if len(str(a))==1 and len(str(b))==1:
    if not kiemtra(a) and not kiemtra(b):
        print('NO')
else:
    # print('vao')
    if kiemtra(a):
        a = xoaso(a)
    if kiemtra(b):
        b = xoaso(b)
    if xoaso(c) == a+b:
        print('YES')
    else:
        print('NO')

