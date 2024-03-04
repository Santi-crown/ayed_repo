# A = [32, 15, 45, 12, 40, 20, 20, 37, 13]
#
# #Pre: A y B están ordenadas
# def merge(A=[], B=[]):
#     i, j, result = 0, 0, []
#     while i < len(A) and j < len(B):
#         if A[i] <= B[i]:
#             result.append(A[i])
#             i += 1
#         else:
#             result.append(B[j])
#             j += 1
#     # Alguna de las secuencias tiene restante
#     if i < len(A):
#         result += A[i:]
#     else:
#         result += B[j:]
#     return result
# # pre: A es una secuencia de elementos comparables
# # pos: Los elementos estan ordenados
# def mergeSort(list = []):
#     if len(list) <= 1:
#         return list
#     half = len(list)//2
#     # Dividir
#     left, right = mergeSort(list[:half]), mergeSort(list[half:])
#     # Conquistar
#     result = merge(left, right) #Combinar
#     return result
#
# print(mergeSort(A))
# Se dividió, conquistó y combinó.



# try 1
# A = [32, 15, 45, 12, 40, 20, 20, 37, 13]
#
#
# def merge(A = [], B = []):
#     i, j, result = 0, 0, []
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             result.append(A[i])
#             i += 1
#         else:
#             result.append(B[j])
#             j += 1
#     # Algunas de las secuencias tiene restantes
#     if i <= len(A):
#         result += A[i:]
#     else:
#         result += B[j:]
#     return result
# def mergeSort(A = []):
#     if len(A) <= 1:
#         return A
#     half = len(A)//2
#     left, right = mergeSort(A[:half]), mergeSort(A[half:])
#
#     result = merge(left, right)
#     return result
# def main():
#     print(mergeSort(A))
# main()

# try 2
# A = [32, 15, 45, 12, 40, 20, 20, 37, 13]
#
# def merge(A = [], B = []):
#     i, j, result = 0, 0, []
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             result.append(A[i])
#             i += 1
#         else:
#             result.append(B[j])
#             j += 1
#     # Alguna de las listas tiene un elemento sobrante
#     if i < len(A):
#         result += A[i:]
#     else:
#         result += B[j:]
#     return result
# def mergeSort(A = []):
#     if len(A) <= 1:
#         return A
#     half = len(A)//2
#
#     # Dividir
#     left, right = mergeSort(A[:half]), mergeSort(A[half:])
#     # Conquistar y comnbinar
#     result = merge(left, right)
#
#     return result
#
# print(mergeSort(A))

# try 3
A = [32, 15, 45, 12, 40, 20, 20, 37, 13]

def merge(A=[],B=[]):
    i,j,result = 0,0,[]
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
        # Hay elementos sobrantes en las sequencias
    if i < len(A):
            result += A[i:]
    else:
            result += B[j:]
    return result
def mergeSort(A=[]):
    if len(A) <= 1:
        return A

    half = len(A)//2
    # Dividir
    left, right = mergeSort(A[:half]), mergeSort(A[half:])

    # Conquistar y combinar
    result = merge(left,right)

    return result

print(mergeSort(A))



# try 4

# try 5