s = input()
s = ' '+s+' '
st = ''
for i in range(1,len(s)):
    if s[i-1] == ' ':
        if s[i] != ' ':
            st+=s[i] 
    else:
        st+=s[i]
print(st[:-1])
    
    