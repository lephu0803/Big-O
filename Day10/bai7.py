class Staff:
    def __init__(self, idx=0, name=0, year=0):
        self.idx = idx
        self.name = name 
        self.year = year

    def get_year(self):
        return int(self.year)
    
    def get_idx(self):
        return int(self.idx)

    def __str__(self):
        return '{} {} {}'.format(self.idx, self.name, self.year)

if __name__ == "__main__":
    n  = int(input())
    if n == 1:
        idx, name, age = map(str, input().split())
        print('{} {} {}'.format(idx, name, age))
    else:
        idx, name, year = map(str, input().split())
        x = Staff(idx, name, year)
        for i in range(1,n):
            idx, name, year = map(str, input().split())
            if int(year) < x.get_year():
                x = Staff(idx, name, year)
            elif int(year) == x.get_year():
                if int(idx) < x.get_idx():
                    x = Staff(idx, name, year)
        print(x)

