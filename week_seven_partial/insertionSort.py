# START = 1
# def insertionSortElement(new_el, sequence):
#     index = 0
#     while index < len(sequence) and new_el > sequence[index]:
#         index+=1
#     return sequence[:index] + [new_el] + sequence[index:]
#
# def insertionSort(A):
#     for index in range(START,len(A)):
#         elem = A[index]
#         A = insertionSortElement(elem, A[:index]) + A[index+1:]
#     return A

# try 1
# def insertionSortElement(new_el,sequence):
#     index = 0
#     while index < len(sequence) and new_el > sequence[index]:
#         index+=1
#     return sequence[:index] + [new_el] + sequence[index:]
#
# def insertionSort(sequence):
#     for index in range(1,len(sequence)):
#         sequence = insertionSortElement(sequence[index],sequence[:index]) + sequence[index+1:]
#     return sequence
#

# try 2
# def insertionSortElement(new_el,sequence):
#     index = 0
#     while index < len(sequence) and new_el > sequence[index]:
#         index += 1
#     return sequence[:index] + [new_el] + sequence[index:]
#
# def insertionSort(sequence):
#     for index in range(1,len(sequence)):
#         sequence = insertionSortElement(sequence[index],sequence[:index]) + sequence[index+1:]
#    return sequence

def insertionSortElement(sequence,element):
    index = 0
    while index < len(sequence) and sequence[index] < element:
        index += 1
    return sequence[:index] + [element] + sequence[index:]
def insertionSort(seq):
    result = seq[:1]
    for i in range(1,len(seq)):
        result = insertionSortElement(result,seq[i])
    return result
print(insertionSort([4,1,9,3,101,66,8,100]))
#