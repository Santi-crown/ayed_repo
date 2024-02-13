def array(list = []):
    if len(list) <=1:
        return list
    list[ len(list) -1] + array(list.remove(len(list-1)))

print(array([1,2,3,4,5,6]))