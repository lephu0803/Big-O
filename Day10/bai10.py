class Apple(object):
    def __init__(self, idx=0, w=0, v=0):
        self.idx = idx
        self.w = w
        self.v = v
    
    def __getattribute__(self, name):
        return object.__getattribute__(self,name)

if __name__ == "__main__":
    n = int(input())
    x = Apple()
    for i in range(n):
        w, v = map(int, input().split())
        if w > x.w:
            x = Apple(i, w, v)
        elif w == x.w:
            if v > x.v:
                x = Apple(i, w, v)
    print(x.idx)
