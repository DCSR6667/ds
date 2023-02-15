'''
17.      1
        212
       32123
      4321234
       32123
        212
         1

'''

def pattern17(rows):
        i=1
        while i<=2*rows-1:
                j=1
                cols=2*rows-i if  i>rows else i
                spaces=i-rows if i>rows else rows-i
                while j<=spaces:
                        print(" ",end=" ")
                        j+=1
                j=cols
                while j>=1:
                        print(j,end=" ")
                        j-=1
                j=2
                while j<=cols:
                        print(j,end=" ")
                        j+=1
                print()
                i+=1

rows=int(input("enter required number of rows"))
pattern17(rows)
                
    
    
    

            