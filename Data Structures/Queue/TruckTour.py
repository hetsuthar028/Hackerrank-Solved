def truckTour(petrolPumps):
    mainQueue = []
    prevRemQueue = []
    total = 0

    for petrolPump in petrolPumps:
        if (total + petrolPump[0] - petrolPump[1]) >=0:
            total += (petrolPump[0] - petrolPump[1])
            mainQueue.append(petrolPump)
            
        else:
            prevRemQueue.extend(mainQueue)
            mainQueue = []
            prevRemQueue.append(petrolPump)
            total = 0
    
    for remPetrolPump in prevRemQueue:
        if (total + remPetrolPump[0] - remPetrolPump[1]) >=0:
            total += (remPetrolPump[0] - remPetrolPump[1])
            mainQueue.append(remPetrolPump)

    return petrolPumps.index(mainQueue[0])


print(truckTour([[1,5],[10,3],[3,4]]))


# if __name__ == "__main__":
#     mainList = []
#     with open('./TruckTourTestCases.txt', 'r') as fp:
#         n = int(fp.readline())
#         for i in range(n):
#             mainList.append(list(map(int, fp.readline().split())))
#     print(mainList)

#     print(truckTour(mainList))