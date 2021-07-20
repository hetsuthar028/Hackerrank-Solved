import math
def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    max = -math.inf
    for i in queries:
        for j in range(i[0]-1, i[1]):
            arr[j] += i[-1]
            if arr[j] > max:
                max = arr[j]
    return max

print(arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]]))