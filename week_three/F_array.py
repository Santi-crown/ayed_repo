from sys import stdin

def array(list):                                    # costo   pasos
    if len(list) <= 1:                              #   1       1
        return list                                 #   1       1

    element = list[(len(list) - 1)]
    list.remove(element)                            #   n       1
    return [element] + array(list) # invariante     #   n       n
                                                    # Total O = (n)
line = stdin.readline().strip().split()
while len(line) > 0:
    # Map each string as int
    print(list(map(int,array(line))))
    line = stdin.readline().strip().split()
