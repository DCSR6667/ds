def getmedian(arr1,arr2,sa,ea,sb,eb):
    if ((ea-sa==1) and (eb-sb==1)):
        return (max(arr1[sa],arr2[sb])+min(arr1[ea]+arr2[eb]))//2
    m1_index=(sa+ea)//2
    m2_index=(sb+eb)//2
    m1=arr1[m1_index]
    m2=arr2[m2_index]
    if m1==m2:
        return m2
    if m1<m2:
        sa=m1_index
        ea=m2_index
    elif m1>m2:
        sb=m2_index
        ea=m1_index
    return getmedian(arr1,arr2,sa,ea,sb,eb)

arr1=[1,12,15,26,38]
arr2=[2,13,17,30,45]
print(getmedian(arr1,arr2,0,len(arr1)-1,0,len(arr2)-1))