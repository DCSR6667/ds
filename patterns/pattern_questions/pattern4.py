'''

4.  1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5  

'''

def pattern4(rows):
    i=1
    while i<=rows:
        j=1
        while j<=i:
            print(j,end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern4(rows)