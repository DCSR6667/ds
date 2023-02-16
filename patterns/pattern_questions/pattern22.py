'''
22.    1
       0 1
       1 0 1
       0 1 0 1
       1 0 1 0 1
'''

def pattern22(rows):
       i=1
       num=1
       while i<=rows:
              num=0 if i%2==0 else 1
              j=1
              while j<=i:
                     print(num,end=" ")
                     num=0 if num==1 else 1
                     j+=1
              print()
              i+=1
rows=int(input("enter required number of rows"))
pattern22(rows)