s1 = input()
a = s1.split(' ')
# print(len(a))
s = ''
for i in reversed(range(len(a))):
    s += a[i]+' '

print(s[:-1])