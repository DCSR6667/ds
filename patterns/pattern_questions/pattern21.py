'''
21.    1
       2  3
       4  5  6
       7  8  9  10
       11 12 13 14 15
'''

def pattern21(rows):
       i=1
       num=1
       while i<=rows:
              j=1
              while j<=i:
                     print(num,end=" ")
                     num+=1
                     j+=1
              print()
              i+=1
rows=int(input("enter required number of rows"))
pattern21(rows)
    