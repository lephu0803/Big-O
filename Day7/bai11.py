n = int(input())
s = input()
# 97
diction = [0 for i in range(26)]
count = 0
if n>26:
    print('-1')
else:
    for char in s:
        diction[ord(char)-97]+=1
    for num in diction:
        if num>1:
            count+=num-1
    print(count)
    
