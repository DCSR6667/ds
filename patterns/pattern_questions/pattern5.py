'''

5.  *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *

'''

def pattern5(rows):
    i=1
    while i<=(2*rows)-1:
        j=1
        cols=2*rows-i if i>rows else i
        while j<=cols:
            print("*",end=" ")
            j+=1
        print()
        i+=1

rows=(int(input("enter required number of rows")))
pattern5(rows)

