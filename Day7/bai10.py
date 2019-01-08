n = int(input())
s = input()
ss = 'QWERTYUIOPASDFGHJKLZXCVBNM'
flag = False
if n < 26:
    flag = False
else:
    s = s.upper()
    for char in s:
        if ss.find(char) != -1:
            ss = ss.replace(char,'')
            if len(ss)==0:
                flag=True
                break
            
if flag:
    print('YES')
else: 
    print('NO')
        
            
        
        
