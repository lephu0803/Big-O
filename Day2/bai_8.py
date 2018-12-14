import math 

n, m, a= map(int, input().split())
# print( n, m)
w = math.ceil(n/a)
h = math.ceil(m/a)
print(w*h)