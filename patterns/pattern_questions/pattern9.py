'''


9.  *********
     *******
      *****
       ***
        *

'''

def pattern9(rows):
    i=1
    while i<=rows:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=(2*rows)-(2*i)+1:
            print("*",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern9(rows)