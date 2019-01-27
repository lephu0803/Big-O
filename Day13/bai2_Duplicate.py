def findDuplicate(string):
    Upper='QWERTYUIOPASDFGHJKLZXCVBNM'
    lower='qwertyuiopasdfghjklzxcvbnm'
    for i in string:
        if (int(Upper.find(i)) == -1):
            if int(lower.find(i)) == -1:
                print(i)
                return False
            else:
                lower = lower.replace(i,'')
        else:
            Upper=Upper.replace(i,'')
    # print(Upper)
    # print(lower)
    return True

if __name__ == "__main__":
    s = input()
    if findDuplicate(s):
        print('null')
        