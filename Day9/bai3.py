def count(n):
    if n//10==0:
        return 1
    else: 
        return 1+count(n//10)
    
if __name__ == "__main__":
    n = int(input())
    print(count(n))
