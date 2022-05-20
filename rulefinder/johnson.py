import numpy as np

def johnson(indMatrix):
    rows = len(indMatrix)
    cols = len(indMatrix[0])
    atrs = len(indMatrix[0][0])
    usefulCells = [[True] * cols for _ in range(rows)]
    usefulCellsCount = cols * rows
    reduct = []

    atrCount = [0] * atrs
    for row in range(rows):
        for col in range(cols):
            for i in range(atrs):
                if indMatrix[row][col][i]:
                    atrCount[i] += 1

    while usefulCellsCount > 0:
        maxValIndex = 0
        for i in range(1, atrs):
            if atrCount[i] > atrCount[maxValIndex]:
                maxValIndex = i

        reduct.append(maxValIndex)
        atrCount = [0] * atrs
        for row in range(rows):
            for col in range(cols):
                if usefulCells[row][col]:
                    if indMatrix[row][col][maxValIndex]:
                        usefulCells[row][col] = False
                        usefulCellsCount -= 1
                    else:
                        for i in range(atrs):
                            if indMatrix[row][col][i]:
                                atrCount[i] += 1

    return reduct