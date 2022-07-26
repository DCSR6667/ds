def product(x,y):
    if y==0:
        return 0
    if x<y:
        return product(y,x)
    return x+product(x,y-1)

print(product(5,600))