import numpy as np

def indist(decMatrix):
    rowCount = decMatrix.shape[0]
    atrCount = decMatrix.shape[1] - 1
    trueArray = []
    falseArray = []
    for i in range(0, rowCount):
        if decMatrix[i,-1]:
            trueArray.append(i)
        else:
            falseArray.append(i)

    rows = len(trueArray)
    cols = len(falseArray)
    indMatrix = [[None] * cols for _ in range(rows)]

    for row in range(0, rows):
        for col in range(0, cols):
            indMatrix[row][col] = [False] * atrCount
            for i in range(atrCount):
                if(decMatrix[trueArray[row]][i] ^ decMatrix[falseArray[col]][i]):
                    indMatrix[row][col][i] = True

    return indMatrix, trueArray, falseArray




