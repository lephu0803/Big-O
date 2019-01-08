
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    
    def distance(self, p2):
        dis = (self.x - p2.x)**2 + (self.y-p2.y)**2
        return dis 

    def __str__(self):
        s = '{} {}'.format(self.x, self.y)
        return s

if __name__ == '__main__':
    x, y = map(int, input().split())
    p1 = Point(x,y)
    n = int(input())
    maxx = 0
    p_max = Point()
    for i in range(n):
        x, y = map(int, input().split())
        p2 = Point(x,y)
        dis = p1.distance(p2)
        if dis > maxx:
            p_max = p2
            maxx = dis
    print(p_max)
