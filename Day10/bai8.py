class Unit(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y 
        self.value = value

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return '{} {}'.format(self.x, self.y)
    
if __name__ == "__main__":
    h,w = map(int, input().split())
    n = int(input())
    a = []
    count = 0
    for i in range(n):
        x, y, value = map(int,input().split())
        if value > 0:
            count+=1
            a.append(Unit(x,y,value))
    print(count)
    for i in a:
        print(i)