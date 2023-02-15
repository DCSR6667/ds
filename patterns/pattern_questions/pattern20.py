'''

20.    ****
       *  *
       *  *
       *  *
       ****
'''

def pattern20(rows):
       i=1
       while i<=rows:
              j=1
              while j<=rows-1:
                     if i==1 or i==rows:
                            print("*",end=" ")
                     else:
                            if j==1 or j==rows-1:
                                   print("*",end=" ")
                            else:
                                   print(" ",end=" ")
                     j+=1
              print()
              i+=1

rows=int(input("enter required number of rows"))
pattern20(rows)
