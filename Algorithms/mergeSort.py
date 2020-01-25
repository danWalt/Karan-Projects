# mergeSort.py is my own implementation of the merge sort sorting algorithm


def mergeSort(numberslist):
    if len(numberslist) <= 1:
        return numberslist
    else:
        middle = len(numberslist) // 2
        left = mergeSort(numberslist[:middle])
        right = mergeSort(numberslist[middle:])
        leftarraypointer = 0
        rightarraypointer = 0
        finallistpointer = 0

        while leftarraypointer < len(left) and rightarraypointer < len(right):
            if left[leftarraypointer] <= right[rightarraypointer]:
                numberslist[finallistpointer] = left[leftarraypointer]
                leftarraypointer += 1
                finallistpointer += 1
            else:
                numberslist[finallistpointer] = right[rightarraypointer]
                rightarraypointer += 1
                finallistpointer += 1
        while leftarraypointer < len(left):
            numberslist[finallistpointer] = left[leftarraypointer]
            leftarraypointer += 1
            finallistpointer += 1
        while rightarraypointer < len(right):
            numberslist[finallistpointer] = right[rightarraypointer]
            rightarraypointer += 1
            finallistpointer += 1
    return numberslist
