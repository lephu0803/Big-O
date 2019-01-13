def T(n):
    if n == 0:
        return 1
    else:
        return n*T(n-1)

if __name__ == "__main__":
    n = int(input())
    print(T(n))