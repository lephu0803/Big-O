class BangMau:
    def __init__(self, idx=0, l=0, count=1):
        self.idx = idx
        self.l = l 
        self.count = count
    def sum_length(self, p):
        self.l = self.l + p.l
        self.count+=1

    def get_color(self):
        return self.idx
    
    def __str__(self):
        return '{} {} {}'.format(self.idx, self.l, self.count)


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        color, length = map(int,input().split())
        # print(BangMau(color, length))
        a.append(BangMau(color, length))
    a.sort(key=lambda x: x.get_color())
    x = a[0]
    for i in range(1,n):
        if a[i].get_color() == a[i-1].get_color():
            x.sum_length(a[i])
        else:
            print(x)
            x = a[i]
    print(x)


