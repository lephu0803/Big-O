s = input()
flag = True
flag_a = None
flag_local = False
flag_domain = False
for i in range(len(s)):
    if i == 0:
        if not ( s[i]<='9' and s[i]>='0' ) and not ( s[i]>='A' and s[i]<='Z' ) and not (s[i]>='a' and s[i]<='z'):
            flag = False
            break
        continue
    elif i == len(s)-1:
        if s[i] == '.':
            flag = False
            break
    if s[i] == '@':
        if flag_local == False:
            flag = False
            break
        if flag_a is None:
            flag_a = True
            continue
        else:
            flag = False
            break
    if flag_a == True:
        if not (s[i]<='9' and s[i]>='0' ) and not ( s[i]>='A' and s[i]<='Z' ) and not (s[i]>='a' and s[i]<='z'):
            flag = False
            break
        elif s[i] == '.':
            if (s[i-1] == '@' or s[i-1] == '.'):
                flag = False
                break
            else:
                flag_domain = True
    else:
        if ( s[i]<='9' and s[i]>='0' ) or ( s[i]>='A' and s[i]<='Z' ) or (s[i]>='a' and s[i]<='z'):
            flag_local = True
        elif (s[i] =='.' or s[i]=='_'):
            pass
        else:
            flag = False
            break       

if flag == True:
    print('VALID')
else:
    print('INVALID')


        
