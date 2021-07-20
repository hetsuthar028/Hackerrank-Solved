import time

def arrayManipulation(n, queries):
    arr = [0]*n
    for list_element in queries:
        a = list_element[0]-1
        b = list_element[1]-1
        k = list_element[2]
        
        for i in range(a,b+1):
            arr[i]=arr[i]+k

    return max(arr)

print(arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]]))