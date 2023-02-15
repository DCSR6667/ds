'''
7.   *****
      ****
       ***
        **
         *
'''
def pattern7(rows):
    i=1
    while i<=rows:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=rows-i+1:
            print("*",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern7(rows)