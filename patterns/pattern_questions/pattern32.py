'''

32.    E
       D E
       C D E
       B C D E
       A B C D E

'''

def pattern32(rows):
    i=1
    
    while i<=rows:
        j=1
        c=chr(65+(rows-i))
        while j<=i:
            print(c,end=" ")
            c=chr(ord(c)+1)
            j+=1
        print()
        i+=1

rows=int(input("enter required number of rows"))
pattern32(rows)
