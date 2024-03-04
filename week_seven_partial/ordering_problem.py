START = 1
list = [("Juan", 25), ("María", 30), ("Pedro", 20), ("Luisa", 18)]

def addElement(element, seq):
    index_element = 0
    while index_element < len(seq) and  seq[index_element][1] < element[1]:
        index_element += 1
    return seq[:index_element] + [element] + seq[index_element:]

def insertionSort(seq):
    result = seq[:START]
    for e in range(START, len(seq)):
        result = addElement(seq[e], result)
    return result
order_list = insertionSort(list)

print(order_list)
print("Nombre de la persona más joven: ", order_list[0][0])


