'''

25.       *****
         *   *
        *   *
       *   *
      *****


'''

def pattern25(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=rows:
            if i==1 or i==rows:
                print("*",end=" ")
            else:
                if j==1 or j==rows:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            j+=1
        print()
        i+=1

rows=int(input("enter required number of rows"))
pattern25(rows)