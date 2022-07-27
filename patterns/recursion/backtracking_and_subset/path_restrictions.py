'''this problem can be solved by subset pattern'''
def path_restrictions(ans,r,c,maze):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(ans)
        return 
    if maze[r][c]==False:
        return
    if r<len(maze)-1:
        path_restrictions(ans+"D",r+1,c,maze)
    if c<len(maze[0])-1:
        path_restrictions(ans+"R",r,c+1,maze)
        
def path_restrictions1(ans,r,c,maze):
    if r==len(maze)-1 and c==len(maze[0])-1:
        l=[]
        l.append(ans)
        return l 
    if maze[r][c]==False:
        return []
    lis=[]
    if r<len(maze)-1:
        lis=lis+path_restrictions1(ans+"D",r+1,c,maze)
    if c<len(maze[0])-1:
        lis=lis+path_restrictions1(ans+"R",r,c+1,maze)
    return lis

maze=[[True,True,True],[True,False,True],[True,True,True]]
print(path_restrictions1("",0,0,maze))
