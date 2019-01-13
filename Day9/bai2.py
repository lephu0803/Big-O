def UL(n):
    if n%2 == 1:
        return int(n)
    else:
        return(UL(n/2))

if __name__ == "__main__":
    n = int(input())
    print(UL(n))