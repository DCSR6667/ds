''' 
14.  *********
      *     *
       *   *
        * *
         *
'''

def pattern14(rows):
    i=1
    while i<=rows:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=(2*rows)-(2*i)+1:
            if i==1 or i==(2*rows)-(2*i)+1:
                print("*",end=" ")
            else:
                if j==1 or j==(2*rows)-(2*i)+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            j+=1
        print()
        i+=1

rows=int(input("enter required number of rows"))
pattern14(rows)
