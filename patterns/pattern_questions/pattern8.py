'''

8.      *
       ***
      *****
     *******
    *********


'''

def pattern8(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=(2*i)-1:
            print("*",end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))        
pattern8(rows)