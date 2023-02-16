''' 

28.      *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''

def pattern28(rows):
    i=1
    while i<=2*rows-1:
        j=1
        cols=(2*rows-2*(i%rows)-1) if i>rows else (2*i-1)
        spaces=(i-rows) if i>rows else (rows-i)
        while j<=spaces:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            if j%2!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern28(rows)