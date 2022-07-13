def allpaths(ans,r,c,maze,path,step):
    if r==len(maze)-1 and c==len(maze[0])-1:
        path[r][c]=step
        for i in path:
            print(i)
        print(ans)
        print()
        return 
    if maze[r][c]==False:
        return
    maze[r][c]=False
    path[r][c]=step
    if r<len(maze)-1:
        allpaths(ans+"D",r+1,c,maze,path,step+1)
    if c<len(maze[0])-1:
        allpaths(ans+"R",r,c+1,maze,path,step+1)
    if r>0:
        allpaths(ans+"U",r-1,c,maze,path,step+1)
    if c>0:
        allpaths(ans+"L",r,c-1,maze,path,step+1)
    maze[r][c]=True
    path[r][c]=0


maze=[[True,True,True],[True,True,True],[True,True,True]]
path=[[0,0,0],[0,0,0],[0,0,0]]
allpaths("",0,0,maze,path,1)