START = 1

def addElement(element, seq):
    element_index = 0
    while not (seq[element_index] > element):
        element_index = element_index + 1
    return seq[:element_index] + [element] + seq[element_index:] # is a sugar syntax to conveniently slice a list.

def insertionSort(seq):
    result = seq[:START]
    for e in range(START,len(seq)):
        # print( result)
        # print(seq[e],result)
        # print (result)
        result = addElement(seq[e], result)
        # print(result)
        # print( result)
    return result
# def main():
print(insertionSort([4,3,2,1,-5]))
# main()