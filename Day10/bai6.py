class BangMau:
    def __init__(self, idx, l):
        self.idx = idx
        self.l = l 
    
    def sum_length(self, p):
        self.l = self.l + p.l

if __name__ == "__main__":
    n = int(input())
