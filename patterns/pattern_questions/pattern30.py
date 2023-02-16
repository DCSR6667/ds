''' 
30.         1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
'''


def pattern30(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows-i:
            print(" ",end=" ")
            j+=1
        j=i 
        while j>=1:
            print(j,end=" ")
            j-=1
        j=2
        while j<=i:
            print(j,end=" ")
            j+=1
        print()
        i+=1

rows=int(input("enter required number of rows"))
pattern30(rows)
