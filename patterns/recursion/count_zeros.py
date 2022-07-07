def count_zeros(n):
    count=0
    if n==0:
        return 0
    if (n%10)==0:
        count+=1
    return count+count_zeros(n//10)
print(count_zeros(1111))