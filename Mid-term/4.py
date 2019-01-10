def check_sudoku(x):
    value = len(x)
    for row in x:
        if len(row) != len(x):
            return False
    for row in x:
        for thing in row:
            if thing>len(x):
                return False
            elif isinstance(thing,float) or thing<1:
                return False

    while value>0:
        for row in x:
            for thing in row:
                if row.count(thing) > 1:
                    return False;
                else:
                    value-=1

    value = len(x)
    eachRow = []

    while value>0:
        for row in x:
            eachRow.append(row[value-1])
        for thing in eachRow:
            if thing > len(x):
                return False
            elif eachRow.count(thing) > 1:
                return False
            elif isinstance(thing,float) or thing<1:
                return False
            else:
                eachRow = []
                value-=1
        return True

a = []
for i in range(9):
    row = []
    row.extend(list(map(int, input().split(' '))))
    a.append(row)

if check_sudoku(a):
    print('YES')
else:
    print('NO')