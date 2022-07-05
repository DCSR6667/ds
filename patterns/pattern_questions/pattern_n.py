'''pattern_31
    1..first consider a wall
    2.. val=min of distances(left,right,top,down) from the wall'''
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

def pattern_13(n):
    i=1
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=2*i-1:
            if i==1 or i==n:
                print("*",end=" ")
            else:
                if j==1 or j==2*i-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            j+=1
        print()
        i+=1


def pattern_14(n):
    i=1
    while i<=n:
        j=1
        while j<=i-1:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=2*n-2*i+1:
            if i==1 or i==n:
                print("*",end=" ")
            else:
                if j==1 or j==2*n-2*i+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            j+=1
        print()
        i+=1

def pattern_15(n):
    i=1
    while i<=2*n-1:
        cols=2*n-2*(i%n)-1 if i>n else 2*i-1
        spaces=i-n if i>n else n-i
        j=1
        while j<=spaces:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=cols:
            if j==1 or j==cols:
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


def pattern_20(n):
    i=1
    while i<=n:
        j=1
        while j<=n-1:
            if i==1 or i==n:
                print("*",end=" ")
            else:
                if j==1 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
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

def pattern_22(n):
    i=1
    while i<=n:
        if i%2!=0:
            num=1
        else:
            num=0
        j=1
        while j<=i:
            print(num,end=" ")
            num=num^1

            j+=1
        print()
        i+=1

def pattern_25(n):
    i=1 
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=" ")
            j+=1
        j=1
        while j<=n:
            if i==1 or i==n:
                print("*",end=" ")
            else:
                if j==1 or j==n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
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
        cols=2*n-2*(i%n)-1 if i>n else 2*i-1
        spaces=i-n if i>n else n-i
        j=1
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



def pattern_31_1(n):
    i=1
    while i<=2*n-1:
        j=1
        while j<=2*n-1:
            dis=(min(min(i,j),min(2*n-i,2*n-j)))
            print(dis,end=" ")
            j+=1
        print()
        i+=1

def pattern_31_2(n):
    i=1
    while i<=2*n-1:
        j=1
        while j<=2*n-1:
            dis=n-(min(min(i,j),min(2*n-i,2*n-j)))+1
            print(dis,end=" ")
            j+=1
        print()
        i+=1

pattern_31_1(4)