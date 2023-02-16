'''
26.   1 1 1 1 1 1
      2 2 2 2 2
      3 3 3 3
      4 4 4
      5 5
      6
'''

def pattern26(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows-i+1:
            print(i,end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern26(rows)
