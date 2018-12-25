n = int(input())

# print(maso)
ten = []
for i in range(n):
    maso = [0 for i in range(26)]
    c = input()
    c = c.upper()
    for char in c:
        if ord(char)>=ord('A') and ord(char)<=ord('Z'):
            maso[ord(char)-65] = maso[ord(char)-65]+1
        # print(maso)
        minn = 1000000
        for i in range(26):
            if maso[i] != 0 and maso[i] < minn:
                minn = maso[i]
                idx = i
    # print(maso)
    ten.append(chr(idx+65).upper())
for i in ten:
    print(i)