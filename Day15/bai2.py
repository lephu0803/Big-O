class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

class AdjacencyMatrix:
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.n = size

    def undirectEdgeList(self):
        edge_list = []
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if self.matrix[i][j] == 1:
                    e = Edge(i,j)
                    edge_list.append([e.u, e.v])
        return edge_list

    def isUndirectmatrix(self):
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

if __name__ == "__main__":
    n = int(input())
    a = [] 
    for i in range(n):
        x = list(map(int, input().split()))
        a.append(x)
    m = AdjacencyMatrix(a,n)
    if m.isUndirectmatrix():
        print('YES')
    else:
        print('NO')