def findMax(n, maxx=0):
    if n//10==0:
        if n%10 > maxx:
            maxx = n%10
        return maxx
    else: 
        if n%10 > maxx:
            maxx = n%10
        findMax(n//10)

if __name__ == "__main__":
    
    n = int(input())
    print(findMax(n))
    