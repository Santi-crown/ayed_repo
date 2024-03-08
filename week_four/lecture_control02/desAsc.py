from sys import stdin
def merge(A = [],B = []):
    i, j, result = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    # Alguna de las sequencias tienen elementos sobrantes
    if i < len(A):
        result += A[i:]
    else:
        result += B[j:]
    return result

def mergeSort(seq):
    if len(seq) == 1:
        return seq
    # Dividir
    half = len(seq) // 2
    left, right = mergeSort(seq[:half]), mergeSort(seq[half:])
    # conquistamos y combinamos
    result = merge(left, right)
    return result

def main():
    line = stdin.readline().strip()
    while line:
        lista = list(map(int,line.split()))
        minNumbre = min(lista)
        print(lista)
        print(minNumbre)
        line = stdin.readline().strip()
main()
