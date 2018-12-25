def chuanhoa(sting):
    st=''
    s = ' '+ sting.lower()
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            st+=s[i].upper()
        else:
            st+=s[i]
    return st

n = int(input())
ten = []
for i in range(n):
    c = input()
    ten.append(chuanhoa(c))

for i in ten:
    print(i)
    