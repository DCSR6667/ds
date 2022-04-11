def common_elements(arr,m,n):
    dict={}
    for i in range(n):
        dict[arr[0][i]]=1
    for i in range(1,m):
        for j in range(n):
            if arr[i][j] in dict.keys() and dict[arr[i][j]]==i:
                dict[arr[i][j]]+=1
    for i in dict.keys():
        if dict[i]==m:
            print(i,end=' ')
arr= [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
common_elements(arr,4,5)