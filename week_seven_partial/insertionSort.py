# Example
# START = 1
# def addElement(element, seq):
#     element_index = 0
#     while not (seq[element_index] > element):
#         element_index = element_index + 1
#     return seq[:element_index] + [element] + seq[element_index:]
# def insertionSort(seq):
#     result = seq[:START]
#     for e in range(START,len(seq)):
#         result = addElement(seq[e], result)
#     return result
# print(insertionSort([4,3,2,1,-4]))


# Try 1
# START = 1

# def addElement(element, seq):
#     element_index = 0
#     while seq[element_index] < element:
#         element_index += 1
#     return seq[:element_index] + [element] + seq[element_index:]
#
# def insertionSort(seq):
#     result = seq[:START]
#     for e in range(START, len(seq)):
#         result = addElement(seq[e], result)
#     return result
#
# print(insertionSort([4,3,2,1,-5]))

# Try 2
# START = 1

# def addElement(seq,element):
#     element_index = 0
#     while seq[element_index] < element:
#         element_index += 1
#     return seq[:element_index] + [element] + seq[element_index:]
#
# def insertionSort(seq):
#     result = seq[:START]
#     for e in range(START, len(seq)):
#         result = addElement(result, seq[e])
#     return result
#
# print(insertionSort([4,3,2,1,-5]))

# Try 3
#START = 1

# def addElement(element, seq):
#     element_index = 0
#     while seq[element_index] < element:
#         element_index += 1
#     return seq[:element_index] + [element] + seq[element_index:]
#
#
# def insertionSort(seq):
#     result = seq[:START]
#     for e in range(START, len(seq)):
#         result = addElement(seq[e], result)
#     return result
#
#
# print(insertionSort([4,3,2,1,-5]))

# Try 4
START = 1
def addElement(element, seq):
    element_index = 0
    while seq[element_index] < element:
        element_index += 1
    return seq[:element_index] + [element] + seq[element_index:]


def insertionSort(seq):
    result = seq[:START]
    for e in range(START,len(seq)):
        result = addElement(seq[e],result)
    return result
print(insertionSort([4,3,2,1,-5]))