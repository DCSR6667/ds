def product_of_digits(n):
    if n==0:
        return 1
    return (n%10)*product_of_digits(n//10)

print(product_of_digits(555))