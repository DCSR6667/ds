'''this problem can be solved by using recursion and back tracking'''
def display(board):
    for i in board:
        for j in i:
            if j:
                print("K",end=" ")
            else:
                print("X",end=" ")
        print()

def isvalid(board,row,col):
    if (row>=0 and row<len(board)) and (col>=0 and col<len(board)):
        return True
    return False

def issafe(board,row,col):
    if isvalid(board,row-2,col-1):
        if board[row-2][col-1]:
            return False
    if isvalid(board,row-2,col+1):
        if board[row-2][col+1]:
            return False
    if isvalid(board,row-1,col-2):
        if board[row-1][col-2]:
            return False
    if isvalid(board,row-1,col+2):
        if board[row-1][col+2]:
            return False

    return True


def knights(board,row):
    if row==len(board):
        display(board)
        print()
        return 1
    count=0
    for col in range(len(board)):
        if issafe(board,row,col):
            board[row][col]=True
            count+=knights(board,row+1)
            board[row][col]=False
    return count

board=[[False,False,False],[False,False,False],
[False,False,False]]
print(knights(board,0))