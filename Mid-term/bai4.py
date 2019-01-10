def isValid(list_num):
    list_num = sorted(list_num)
    for i in range(len(list_num) - 1):
        if list_num[i] == list_num[i+1]:
            return False
    return True

def isValidSquare(arr, stride=3):
    for x in range(0, int(len(arr)/stride)):
        for y in range(0, int(len(arr)/stride)):
            window_arr = []
            for i in range(y*stride, y*stride + stride):
                for j in range(x*stride, x*stride + stride):
                    window_arr.append(arr[i][j])
            
            # print('-----------------------')
            # print(window_arr)
            if not isValid(window_arr):
                return False
    return True

def isValidRow(arr):
    for y in arr:
        if not isValid(y):
            return False
    return True

def isValidColumn(arr):
    for x in range(0, len(arr)):
        row = []
        for y in range(0, len(arr)):    
            row.append(arr[x][y])
        
        if not isValid(row):
            return False
    return True

def isValidResult(arr):
    if not isValidColumn(arr):
        return "NO"
    
    elif not isValidRow(arr):
        return "NO"

    elif not isValidSquare(arr):
        return "NO"

    return "YES"

n = 9
arr = []
for i in range(n):
    row = []
    row.extend(list(map(int, input().split(' '))))
    arr.append(row)

print(isValidResult(arr))