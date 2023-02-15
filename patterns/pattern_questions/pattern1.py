'''
 1. *****
    *****
    *****
    *****
    *****
'''

def pattern1(rows):
    i=1
    while i<=rows:
        j=1
        while j<=rows:
            print('*',end=" ")
            j+=1
        print()
        i+=1
rows=int(input("enter required number of rows"))
pattern1(rows)

