# def poisonousPlants(p):
#     stack = p[::]
#     days = 0
#     deadPlants = 1
#     while deadPlants!=0:
#         temp = []
#         deadPlants = 0
#         temp.append(stack[0])
#         stackLength = len(stack)

#         if stackLength == 1 or stackLength == 0:
#             return days
#         flag = 0

#         for i in range(1, stackLength):
#             if stack[i] > stack[i-1]:
#                 # print(stack[i], stack[i-1])
#                 deadPlants +=1
#                 flag = 1
#             else:
#                 # print(stack[i])
#                 temp.append(stack[i])
#         if flag !=0:
#             days +=1
#         stack = temp[::]    
#         # print(stack)
#         # print("Day", days)

#     return days


def poisonousPlants(p):
    safestPlants = []
    daysCt = 0
    length = len(p)
    normalDead = 0
    # someDead = 0
    # something = 0
    for i in range(length):
        if i == 0:
            safestPlants.append(p[i])
        else:
            x = p[i]
            if p[i] > p[i-1]:
                daysCt = 1
                continue
            else:
                if p[i] > safestPlants[-1]:
                    daysCt +=1
                    continue
                else:
                    # something +=1
                    safestPlants.append(p[i])
    # daysCt +=1
    
    print(safestPlants, normalDead, daysCt)
    return (normalDead + daysCt)//2




    
print("Days: ", poisonousPlants([6,5,8,4,7,10,9]))
print("Days: ", poisonousPlants([6,5,6, 7, 7, 10, 9]))
print("Days: ", poisonousPlants([8, 10, 9, 7, 6, 10, 8]))
print("Days: ", poisonousPlants([6,5,4,5,7,6,2,8,7,5]))
print("Test")
print("Days: ", poisonousPlants([4,3,7,5,6,4,2]))

