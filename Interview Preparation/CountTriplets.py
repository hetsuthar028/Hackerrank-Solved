# def countTriplets(arr, r):
#     counts = {}
#     length = 0
#     for i in arr:
#         length +=1
#         if i not in counts:
#             counts[i] = 1
#         else:
#             counts[i] +=1
#     ct = 0
#     for i in range(length - 3 +1):
#         # arr[i], arr[i+1], arr[i+2]
#         # first = arr[i]
#         # second = arr[i]*r
#         # third = arr[i]*r*r
#         print(ct)
#         ct += counts[arr[i]]*counts[arr[i]*r]*counts[arr[i]*r*r]
#     print(ct)

def countTriplets(arr, r):
    counts = {}
    uniqueCount = 0
    for i in arr:
        if i in counts:
            counts[i]+=1
        else:
            uniqueCount +=1
            counts[i] = 1
    finalSum = 0
    s = 0
    for i in range(100- 3 +1):
        print(i)
        s+=1
        finalSum += counts[arr[i]]*counts[arr[i]*r]*counts[arr[i]*r*r]
    print(s)
    print(finalSum)

countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1)