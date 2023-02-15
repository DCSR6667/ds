''''
10.      *
        * *
       * * *
      * * * *
     * * * * *

'''

def pattern10(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=(2*i)-1:
            if j%2!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern10(rows)