def chuanhoa(sting):
    st=''
    s = '  '+ sting
    for i in range(2,len(s)):
        if s[i-1] == ' ' and s[i-2] =='.':
            st+=s[i].upper()
        else:
            st+=s[i]
    return st

s = input()
# print(len(s))
print(chuanhoa(s))
# print(len(chuanhoa(s)))