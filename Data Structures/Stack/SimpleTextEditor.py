q = int(input())
prevOperations = []
s = ""
prevDeletedData = []
ans = []

for i in range(q):
    operation = input().split()
    if operation[0] == "1":
        s += operation[1]
        prevOperations.append(operation)
    if operation[0] == "2":
        k = int(operation[1])
        prevOperations.append(operation)
        prevDeletedData.append(s[len(s)-k:])
        s = s[: len(s)-k]
    if operation[0] == "3":
        k = int(operation[1])
        ans.append(s[k-1])
    if operation[0] == "4":
        if prevOperations[-1][0] == "1":
            s = s[:len(s)-len(prevOperations[-1][1])]
        if prevOperations[-1][0] == "2":
            s += prevDeletedData[-1]
            prevDeletedData.pop(-1)
        prevOperations.pop(-1)

    
for i in ans:
    print(i)