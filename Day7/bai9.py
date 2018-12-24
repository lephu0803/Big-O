s1 = input()
s2 = input()
s3 = input()
a1 = [0 for i in range(26)]
a2 = [0 for i in range(26)]
for char in s1:
    a1[ord(char)-65]+= 1
for char in s2:
    a1[ord(char)-65]+= 1
# print(a1)
for char in s3:
    a2[ord(char)-65]+= 1
if a1 == a2:
    print('YES')
else:
    print('NO')