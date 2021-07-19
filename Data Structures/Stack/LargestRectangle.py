def largestRectangle(n):
    n = sorted(n)
    length = len(n)
    largestRect = 0
    for i in range(length):
        currentRect = n[i]*(length-i)
        if currentRect > largestRect:
            largestRect = currentRect
    return largestRect

print(largestRectangle([1,2,3,4,5]))