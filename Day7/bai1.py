n = int(input())
chars = 'bigo'
a = []
def kiemtra(s):
    s = s.lower()
    for char in s:
        if char == 'b' or char == 'i' or char == 'g' or char == 'o':
            return True
            break
    return  False
for i in range(n):
    s = input()
    if kiemtra(s):
        a.append('YES')
    else:
        a.append('NO')
for i in a:
    print(i)
