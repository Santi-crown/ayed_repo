START = 1

def addElement(seq,element):
    element_index = 0
    while (seq[element_index] <= element):
        element_index = element_index + 1
    return seq[:element_index] + [element] + seq[element_index:]

def insertionSort(seq):
    result = seq[:START]
    for e in range(START, len(seq)):
        result = addElement(result,seq[e])
    return result

# print(insertionSort([5,4,3,2,1]))
print(insertionSort([3,2,4,5,1]))

# Note, result is the invariant