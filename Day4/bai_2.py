def binh_phuong(a):
    return a**2

n = int(input())
tong = 0
for i in range(1,n+1):
    tong += binh_phuong(i)

print(tong)