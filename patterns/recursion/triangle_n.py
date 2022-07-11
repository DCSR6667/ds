def triangle1(r,c):
    if r==0:
        return
    if c<r:
        print("*",end=" ")
        triangle1(r,c+1)
    else:
        print()
        triangle1(r-1,0)
triangle1(5,0)