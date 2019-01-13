# class Fraction:
#     def __init__(self, a =0, b =1):
#         self.nu = a
#         self.de = b
#     def gcd(self, a, b):
#         r = 0
#         while (b!=0):
#             r = a%b
#             a = b
#             b = r
#         return a 

#     def reduceFraction(self):
#         if self.nu == 0:
#             self.de = 1
#             return
#         x  = self.gcd(abs(self.nu), abs(self.de))
#         self.nu = self.nu//x
#         self.de = self.de//x
#         return '{} {}'.format(self.nu, self.de)
    
#     def isLarger(self,p2):
#         if self.nu*p2.de > self.de*p2.nu:
#             return True
#         else:
#             return False
#     # def sumFraction(self, p2):
#     #     p3 = Fraction()
#     #     p3.nu = self.nu * p2.de + self.de*p2.nu
#     #     p3.de = self.de * p2.de 
#     #     p3.reduceFraction()
#     #     return p3  
#     def __str__(self):
#         return '{} {}'.format(self.nu, self.de)

def gcd(a, b):
    r = 0
    while (b!=0):
        r = a%b
        a = b
        b = r
    return a

def reduce_(a,b):
    x = gcd(a, b)
    nu = a//x
    de = b//x
    return '{} {}'.format(int(nu), int(de))

if __name__ == "__main__":

    n = int(input())
    maxx = 0
    maxx_nu =0
    maxx_de =1
    for i in range(n):
        nu, de = map(float, input().split())
        if nu/de > maxx:
            maxx = nu/de
            maxx_nu = nu
            maxx_de = de
    print(reduce_(maxx_nu,maxx_de))
    
    '''
    a = []
    for i in range(n):
        nu, de = map(int, input().split())
        a.append(Fraction(nu,de))
    maxx = a[0]
    for i in range(1,n):
        if a[i].isLarger(maxx):
            maxx = a[i]
        
    print(maxx.reduceFraction())
    '''