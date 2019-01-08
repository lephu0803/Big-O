s = input()
cnt = 0
for char in s:
    if ord(char)>=ord('0') and ord(char)<=ord('9'):
        cnt+=1
print(cnt)