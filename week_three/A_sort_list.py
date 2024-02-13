def sort_sequence(sequence = [] ):
    if len(sequence) <= 1:
        return sequence
    element = [min(sequence)]
    # como sumamos el minimo al inicio, entonces debemos remover el elemento
    # con posción 0.
    sequence.remove(element[0])
    return element + sort_sequence(sequence) # invariante
print(sort_sequence([-2,4,5,7,9,3,1]))