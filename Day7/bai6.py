c = input()
maso1 = [0 for i in range(26)]
maso2 = [0 for i in range(26)]
for char in c:
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        maso1[ord(char)-65] = maso1[ord(char)-65]+1
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
        maso2[ord(char)-97] = maso2[ord(char)-97]+1
cnt = 0
for i in range(26):
    if maso1[i] !=0:
        cnt+=1
    if maso2[i] !=0:
        cnt+=1
print(cnt)