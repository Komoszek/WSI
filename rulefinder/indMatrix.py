import numpy as np

def indMatrix(atrMatrix, decArray):
    atrCount = atrMatrix.shape[1]
    unique, counts = np.unique(decArray, return_counts=True)
    columns = counts[0]
    rows = counts[1]
    indMatrix = [[None] * (columns + 1) for _ in range(rows + 1)]
    true_iter = 1
    false_iter = 1

    for i in range(len(decArray)):
        if(decArray[i]):
            indMatrix[true_iter][0] = i
            true_iter += 1
        else:
            indMatrix[0][false_iter] = i
            false_iter += 1

    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            indMatrix[row][col] = [False] * atrCount
            for i in range(atrCount):
                if(atrMatrix[indMatrix[row][0]][i] ^ atrMatrix[indMatrix[0][col]][i]):
                    indMatrix[row][col][i] = True

    return indMatrix




