class graph:
    
    def __init__(self,value=None):
        self.g=value
        self.visited=[None for i in range(6)]
    
    def addedge(self,v,e):
        self.g[v].append(e)
    
    
    def bfsal(self,v):
        print(v)
        queue=[v]
        visited=[v]
        while len(queue)!=0:
            p=queue.pop(0)
            for i in self.g[p]:
                if i not in visited:
                    print(i)
                    queue.append(i)
                    visited.append(i)

    def bfsam(self,v,n):
        visited=[None for x in range(n+1)]
        print(chr(64+v))
        queue=[v]
        visited[v]=1
        while len(queue)!=0:
            i=queue.pop(0)
            for j in range(1,n+1):
                if self.g[i][j]==1 and visited[j] is None:

                    print(chr(64+j))
                    visited[j]=1
                    queue.append(j)


    def dfsals(self,v):
        stack=[v]
        visited=[v]
        while len(stack)!=0:
            p=stack.pop()
            print(p)
            for i in self.g[p]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)

    def dfsalr(self,v):
        if v not in self.visited:
            print(v)
            self.visited.append(v)
            for i in self.g[v]:
                self.dfsalr(i)

    def dfsamr(self,v,n):
        if self.visited[v] is None:
            print(chr(64+v))
            self.visited[v]=1
            for i in range(1,n+1):
                if self.g[v][i]==1 and self.visited[i] is None:
                    self.dfsamr(i,n)

    def dfsams(self,v,n):
        visited=[None for x in range(n+1)]
        visited[v]=1
        stack=[v]
        while len(stack)!=0:
            i=stack.pop()
            print(chr(64+i))
            for j in range(1,n+1):
                if self.g[i][j]==1 and visited[j] is None:
                    stack.append(j)
                    visited[j]=1


            



#g={"a":["b","c","d"],"b":["a","c"],"c":["b","d","e"],"d":["a","c","e"],"e":["c","d"]}
g=[[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,1,0,1,0,0],
[0,0,1,0,1,1],
[0,1,0,1,0,1],
[0,0,0,1,1,0]]
g=graph(g)
g.dfsams(ord("A")-64,5)


