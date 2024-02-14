def array(list):
    if len(list) <= 1:
        return list

    element = list[(len(list) - 1)]
    list.remove(element)
    return [element] + array(list) # invariante

print(array([1,2,3,4,5,6]))
