#  Pre condición: la lista tiene que estár ordenada

A = [12, 13, 15, 20, 20, 32, 37, 40, 45]
e = 20
def binSearch(A,e):

    mid = len(A) // 2

    if len(A) == 1 and A[mid] != e or len(A) < 1: # Si buscamos por debajo de la longitud del arreglo
        return False
    if A[mid] == e:
        return True
    return binSearch(A[:mid], e) if e < A[mid] else binSearch(A[mid+1:],e)

print('Searching: ',e, ' in ', A,' : ', binSearch(A,e) )