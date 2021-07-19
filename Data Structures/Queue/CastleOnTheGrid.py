n = 3

def getSuccessors(grid, topElement, distances):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    successors = []

    for i in directions:
        pass
        
    while True:
        if topElement[0] + 1 <n:
            successors.append()

def minimumMoves(grid, startX, startY, goalX, goalY):
    mainQueue = []
    visited = [[None for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]

    distances = [[-1]*len(grid) for _ in range(len(grid))]


    mainQueue.append((startX, startY))
    visited[startX][startY] = 2 # 1 -> If visited | 2 -> Explored Successors
    path[startX][startY] = (startX, startY)
    distances[startX][startY] = 0
    
    while mainQueue:
        topElement = mainQueue.pop(0)
        
        height = distances[topElement[0]][topElement[1]]
        getSuccessors(grid, topElement, distances)

        


    pass