from sys import stdin
def intMat(mat):

    for i in range(len(mat)):
        element = int(mat[i])
        mat[i] = element
    return mat

def inputText():

    sizeMat = inputSizeMat()
    dicDimensionSubBoard = inputCaseSubBoard(sizeMat)
    return sizeMat, dicDimensionSubBoard

def inputSizeMat():

    sizeMat = input("Entrada 1: ")
    sizeMat = sizeMat.split()
    sizeMat = intMat(sizeMat)
    return  sizeMat

def inputCaseSubBoard(sizeMat):

    subBoard = sizeMat[2]
    dicDimensionSubBoard = {}
    for case in range(subBoard):
        dicDimensionSubBoard [case + 1] = (input("Entrada 2: ")).split()
        intMat(dicDimensionSubBoard [case + 1])
    print(dicDimensionSubBoard)
    return dicDimensionSubBoard

def generateMat(sizeMat, dicDimensionSubBoard):

    fila = sizeMat[0]
    colu = sizeMat[1]
    mat = [[0 for fil in range(fila)] for col in range(colu)]
    for fil in range(fila):
        for col in range(colu):
            print(mat[fil][col], end = "")
        print("")
    return mat

def fillMat(mat, dicDimensionSubBoard):
    pass
def main():
    sizeMat, dicDimensionSubBoard = inputText()
    mat = generateMat(sizeMat, dicDimensionSubBoard)
    fillMat(mat, dicDimensionSubBoard)
main()