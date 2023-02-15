'''

2.  *
    **
    ***
    ****
    *****

'''

def pattern2(rows):
    i=1
    while i<=rows:
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern2(rows)
