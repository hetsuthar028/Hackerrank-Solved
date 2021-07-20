def minimumSwaps(arr):
    ct = 0
    getIndex = dict(zip(arr,range(1,len(arr)+1)))
    
    for i in range(1, len(arr)+1):
        if getIndex[i]!=i:
            getIndex[arr[i-1]] = getIndex[i]
            arr[getIndex[i]-1] = arr[i-1]
            ct +=1
    return ct

print(minimumSwaps([7,1,3,2,4,5,6]))