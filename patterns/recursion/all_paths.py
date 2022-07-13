def allpaths(ans,r,c,maze):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(ans)
        return 
    if maze[r][c]==False:
        return
    maze[r][c]=False
    if r<len(maze)-1:
        allpaths(ans+"D",r+1,c,maze)
    if c<len(maze[0])-1:
        allpaths(ans+"R",r,c+1,maze)
    if r>0:
        allpaths(ans+"U",r-1,c,maze)
    if c>0:
        allpaths(ans+"L",r,c-1,maze)
    maze[r][c]=True

def allpaths1(ans,r,c,maze):
    if r==len(maze)-1 and c==len(maze[0])-1:
        l=[]
        l.append(ans)
        return l 
    if maze[r][c]==False:
        return []
    maze[r][c]=False
    lis=[]
    if r<len(maze)-1:
        lis=lis+allpaths1(ans+"D",r+1,c,maze)
    if c<len(maze[0])-1:
        lis=lis+allpaths1(ans+"R",r,c+1,maze)
    if r>0:
        lis=lis+allpaths1(ans+"U",r-1,c,maze)
    if c>0:
        lis=lis+allpaths1(ans+"L",r,c-1,maze)
    maze[r][c]=True
    return lis

maze=[[True,True,True],[True,True,True],[True,True,True]]
print(allpaths1("",0,0,maze))