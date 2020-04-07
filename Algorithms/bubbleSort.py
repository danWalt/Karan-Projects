# bubbleSort.py is my own implementation of the bubble sort sorting algorithm.

def bubbleSort(numList):
    n = len(numList)
    while n > 1:
        for i in range(n - 1):
            print(numList)
            if numList[i] >= numList[i + 1]:
                numList[i], numList[i + 1] = numList[i + 1], numList[i]
        n = n - 1
    return numList


numList = [3, 18, 2, 22, 87, 15, 12, 77, 5]
print(bubbleSort(numList))
