class Student:
    def __init__(self, maso, toan,van):
        self.maso = maso
        self.toan = toan
        self.van = van
    
    def trungbinh(self):
        return (self.toan+self.van)/2
    
    def __str__(self):
        return '{} {}'.format(self.toan, self.van)

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        idx, t, v = map(float, input().split())
        a.append(Student(idx, t, v))
    diem = []
    for idx in range(q):
        ms = float(input())
        for hs in a:
            if hs.maso == ms:
                diem.append(hs)
    for i in diem:
        print(i)     