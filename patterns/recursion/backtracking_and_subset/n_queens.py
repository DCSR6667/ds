'''this problem can be solved by using recursion and back tracking'''
def display(board):
    for i in board:
        for j in i:
            if j:
                print("Q",end=" ")
            else:
                print("X",end=" ")
        print()

def issafe(board,row,col):
    ### checking vertical
    for i in range(row):
        if board[i][col]:
            return False
    ### checking diagonal left
    val1=min(row,col)
    i=1
    while i<=val1:
        if board[row-i][col-i]:
            return False
        i+=1
    ### checking diagonal right
    val2=min(row,len(board)-col-1)
    i=1
    while i<=val2: 
        if board[row-i][col+i]:
            return False
        i+=1
    return True


def queens(board,row):
    if row==len(board):
        display(board)
        print()
        return 1
    count=0
    for col in range(len(board)):
        if issafe(board,row,col):
            board[row][col]=True
            count+=queens(board,row+1)
            board[row][col]=False
    return count

board=[[False,False,False,False],[False,False,False,False],
[False,False,False,False],[False,False,False,False]]
print(queens(board,0))