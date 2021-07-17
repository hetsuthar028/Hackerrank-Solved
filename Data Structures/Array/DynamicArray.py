def dynamicArray(n, queries):
    ans = []
    arr = []
    for i in range(n):
        arr.append([])
    
    lastAnswer = 0
    for i in queries:
        type, x, y  = i[0], i[1], i[2]
        if type == 1:
            idx = (x^lastAnswer)%n
            arr[idx].append(y)
        else:
            idx = (x^lastAnswer)%n
            lastAnswer = arr[idx][y%len(arr[idx])]
            ans.append(lastAnswer)
    return ans

print(dynamicArray(2, ['1 0 5', '1 1 7', '1 0 3', '2 1 0', '2 1 1']))