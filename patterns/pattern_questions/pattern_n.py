def pattern_1(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            print("*",end=" ")
            j+=1
        print()
        i+=1

def pattern_2(n):
    i=1
    while i<=n:
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
        print()
        i+=1

def pattern_3(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i+1:
            print("*",end=" ")
            j+=1
        print()
        i+=1

def pattern_4(n):
    i=1
    while i<=n:
        j=1
        while j<=i:
            print(j,end=" ")
            j+=1
        print()
        i+=1

def pattern_5(n):
    i=1
    while i<=2*n-1:
        j=1
        cols=2*n-i if i>n else i
        while j<=cols:
            print("*",end=" ")
            j+=1
        print()
        i+=1

def pattern_6(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
        print()
        i+=1

 
def pattern_7(n):
    i=1
    while i<=n:
        j=1
        cols=n-i+1
        while j<=n-cols:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            print("*",end=" ")
            j+=1
        print()
        i+=1       

  
def pattern_8(n):
    i=1
    while i<=n:
        j=1
        cols=2*i-1
        while j<=n-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            print("*",end=" ")
            j+=1
        print()
        i+=1 

  
def pattern_9(n):
    i=1
    while i<=n:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=2*n-2*i+1:
            print("*",end=" ")
            j+=1
        print()
        i+=1 
    
def pattern_10(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=2*i-1:
            if j%2!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1

def pattern_11(n):
    i=1
    while i<=n:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=2*n-2*i+1:
            if j%2!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1 

def pattern_12(n):
    i=1
    while i<=2*n:
        j=1
        spaces=2*n-i if i>n else i-1
        cols=2*(n if i%n==0 else i%n)-1 if i>n else 2*n-2*i+1
        while j<=spaces:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            if j%2!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1 

def pattern_17(n):
    i=1
    while i<=2*n-1:
        cols=2*n-i if i>n else i
        j=1
        while j<=n-cols:
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

def pattern_21(n):
    i=1
    num=1
    while i<=n:
        j=1
        while j<=i:
            print(num,end=" ")
            num+=1
            j+=1
        print()
        i+=1

def pattern_26(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i+1:
            print(i,end=" ")
            j+=1
        print()
        i+=1

def pattern_28(n):
    i=1
    while i<=2*n-1:
        cols=2*n-i if i>n else i
        spaces=n-cols
        j=1
        while j<=spaces:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            print("*",end=" ")
            j+=1
        print()
        i+=1



def pattern_30(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i:
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

pattern_21(5)