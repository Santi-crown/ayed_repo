# try 1
# def merge(A, B):
#     i,j,result = 0,0,[]
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             result.append(A[i])
#             i+=1
#         else:
#             result.append(B[j])
#             j += 1
#     # algunas de las subsecuencias tiene elementos sobrantes
#     if i < len(A):
#         result += A[i:]
#     else:
#         result += B[j:]
#     return result
# def mergeSort(sequence):
#     if len(sequence) <= 1:
#         return sequence
#
#     half = len(sequence)//2
#     # dividir
#     left, right = mergeSort(sequence[:half]), mergeSort(sequence[half:])
#     # conquistar y combinar
#     result = merge(left,right)
#     return result

# try 2
# def merge(A,B):
#     i,j,result = 0,0,[]
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             result.append(A[i])
#             i += 1
#         else:
#             result.append(B[j])
#             j += 1
#         # Alguna de las sequencias tiene elementos sobrantes
#     if i < len(A):
#             result += A[i:]
#     else:
#             result += B[j:]
#     return result
# def mergeSort(sequence):
#
#     if len(sequence) <= 1:
#         return sequence
#     # Dividir
#     half = len(sequence)//2
#     left, right = mergeSort(sequence[:half]), mergeSort(sequence[half:])
#     # conquistar y combinar
#     result = merge(left,right)
#     return result

# try 3 - test 10 minutes sucess

def merge(A,B):
    i,j,result = 0,0,[]
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append((B[j]))
            j += 1
    # algunas de las subcadenas tiene elementos restantes
    if i < len(A):
        result += A[i:]
    else:
        result += B[j:]
    return result

def mergeSort(sequence):
    if len(sequence) <= 1:
        return sequence
    # Dividir
    half = len(sequence)//2
    left,right = mergeSort(sequence[:half]),mergeSort(sequence[half:])
    # Conquistar y combinar
    result = merge(left,right)
    return result
A = [32, 15, 45, 12, 40, 20, 20, 37, 13]
print(mergeSort(A))