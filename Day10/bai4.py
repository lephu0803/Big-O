import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    
    def distance(self, p2):
        dis = math.sqrt((self.x - p2.x)**2 + (self.y-p2.y)**2)
        return dis 

    def __str__(self):
        s = '{} {}'.format(self.x, self.y)
        return s

class Triangle:
    def __init__(self, a,b,c):
        self.d1 = a.distance(b)
        self.d2 = b.distance(c)
        self.d3 = c.distance(a)
        # print(self.chuvi)

    def chuvi(self): 
        return self.d1+self.d2+self.d3
    
    def dientich(self):
        s = self.chuvi()/2
        return math.sqrt((s*(s-self.d1)*(s-self.d2)*(s-self.d3)))

if __name__ == "__main__":
    n = int(input())
    tong = 0
    for i in range(n):
        a = []
        x, y = map(int, input().split())
        p1 = Point(x,y)
        x, y = map(int, input().split())
        p2 = Point(x,y)
        x, y = map(int, input().split())
        p3 = Point(x,y)
        triangle = Triangle(p1,p2,p3)
        tong+=triangle.dientich()
    print('{0:.2f}'.format(tong))

