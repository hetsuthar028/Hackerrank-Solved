import math
def getMax(operations):
    stack = []
    ans = []
    maxStack = [-math.inf]

    for i in operations:
        op = list(map(int, i.split()))
        if op[0] == 1:
            if op[1] > maxStack[-1]:
                maxStack.append(op[1])

            stack.append(op[1])

        elif op[0] == 2:
            if stack.pop(-1) == maxStack[-1]:
                maxStack.pop(-1)
        else:
            ans.append(maxStack[-1])
    return ans

print(getMax(['1 10', '1 20', '1 15', '1 30', '2', '3', '1 40', '3']))