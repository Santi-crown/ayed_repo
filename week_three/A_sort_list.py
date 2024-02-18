from sys import stdin

def sort_sequence(sequence = [] ):                                              # costo   pasos
    if len(sequence) <= 1:                                                      #   1       1
        return sequence                                                         #   1       1
    element = [min(sequence)]                                                   #   n       n
    # como sumamos el minimo al inicio, entonces debemos remover el elemento
    # con posción 0.
    sequence.remove(element[0])                                                 #   n       n
    return element + sort_sequence(sequence) # invariante                       #   n*n     n
                                                                                # Total O = (n^2)
line = list(stdin.readline().strip().split())
while len(line) > 0:
    print(sort_sequence(line))
    #with this we can read the next line
    line = list(stdin.readline().strip().split())