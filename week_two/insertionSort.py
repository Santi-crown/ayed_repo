def insertionSortElement(new_el, sequence):
    index = 0
    while index < len(sequence) and new_el > sequence[index]:
        index+=1
    return sequence[:index] + [new_el] + sequence[index:]
#pre: sequence is a list of comparable objects
def insertionSort(sequence):
    #print(sequence)
    for index in range(1,len(sequence)):
        elem = sequence[index]
        #print(elem, str(sequence[:index+1]) + '-->'+ str(insertionSortElement(elem, sequence[:index])), sequence[index+1:], insertionSortElement(elem, sequence[:index]) + sequence[index+1:])
        sequence = insertionSortElement(elem, sequence[:index]) + sequence[index+1:]
    return sequence

print(insertionSort([4,1,9,3,100,66,8,100]))