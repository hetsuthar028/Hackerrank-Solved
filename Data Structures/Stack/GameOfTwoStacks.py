# def twoStacks(maxSum, a, b):
#     stackSum = 0
#     ct = 0
#     n = len(a)
#     m = len(b)
#     while True:
#         try:
#             if a[0] < b[0]:
#                 if stackSum + a[0] <= maxSum:
#                     aPopped = a.pop(0)
#                     print(aPopped)
#                     stackSum += aPopped
#                     ct +=1
#                     n -=1
#                 else:
#                     if stackSum + b[0] <= maxSum:
#                         print(a[0], b[0])
#                         stackSum +=b.pop(0)
#                         ct +=1
#                         m -=1
#                     else:
#                         return ct
#             else:
#                 if stackSum + b[0] <= maxSum:
#                     print(a[0], b[0])
#                     stackSum +=b.pop(0)
#                     ct +=1
#                     m -=1
#                 else:
#                     if stackSum + a[0] <= maxSum:
#                         stackSum +=a.pop(0)
#                         ct +=1
#                         n -=1
#                     else:
#                         return ct
#         except:
#             print("Exception")
#             if n == 0:
#                 for i in range(m):
#                     if stackSum + b[0] <= maxSum:
#                         stackSum +=b.pop(0)
#                         ct +=1
#                     else:
#                         return ct
                 
#             if m == 0:
#                 print("M Eq")
#                 print(stackSum)
#                 for i in range(n):
#                     if stackSum + a[0] <= maxSum:
#                         stackSum +=a.pop(0)
#                         ct +=1
#                     else:
#                         print("MAX", stackSum)
#                         return ct
#             print("MAX", stackSum)                        
#             return ct


def twoStacks(maxSum, a, b):
    bestCount = 0
    sumA = sumB = 0

    i = j = 0

    while i < len(a) and sumA + a[i] <= maxSum:
        sumA += a[i]
        i+=1

    while j < len(b) and sumB + b[j] <= maxSum:
        sumB += b[j]
        j+=1
    
    bestCount = max(i, j)

    if sumB < sumA:
        temp = sumB
        newBest = j
        for ia in range(i):
            if (temp + a[ia] <= maxSum):
                newBest +=1
                temp += a[ia]
        
        bestCount = max(bestCount, newBest)
        
    if sumA < sumB:
        temp = sumA
        newBest = i
        for jb in range(j):
            if (temp + b[jb] <=maxSum):
                newBest +=1
                temp += b[jb]
        
        bestCount = max(bestCount, newBest)
    
    return bestCount

print(twoStacks(10, [4,2,4,6,1], [5,8,8,5]))