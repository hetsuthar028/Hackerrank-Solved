def diagonalDifference(arr):
    diff = 0
    for i in range(n):
        # print(i)
        diff += abs(arr[n*i] - arr[n*n - n - 1])
        print(diff)
    print(diff)

if __name__ == "__main__":
    n = 3
    diagonalDifference([11,2,4,4,5,6,10,8,-12])