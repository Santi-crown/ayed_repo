from sys import stdin

def array(list):
    if len(list) <= 1:
        return list

    element = list[(len(list) - 1)]
    list.remove(element)
    return [element] + array(list) # invariante

line = stdin.readline().strip().split()
while len(line) > 0:
    # Map each string as int
    print(list(map(int,array(line))))
    line = stdin.readline().strip().split()
