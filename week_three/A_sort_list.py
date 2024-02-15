from sys import stdin

def sort_sequence(sequence = [] ):
    if len(sequence) <= 1:
        return sequence
    element = [min(sequence)]
    # como sumamos el minimo al inicio, entonces debemos remover el elemento
    # con posción 0.
    sequence.remove(element[0])
    return element + sort_sequence(sequence) # invariante


line = list(stdin.readline().strip().split())
while len(line) > 0:
    print(sort_sequence(line))
    #with this we can read the next line
    line = list(stdin.readline().strip().split())