from sys import stdin
def findMissingNumber(lista, N):
    # Suma esperada
    total = N * (N + 1) // 2
    # Suma real
    sum_of_elements = sum(lista)
    # El número faltante es la diferencia entre la suma total - la suma esperada
    return total - sum_of_elements
def main():
    line = stdin.readline().strip()
    while line:
        lista = list(map(int,line.split()))
        N = max(lista)  # Assuming that max element is equal to N
        missNumber = findMissingNumber(lista, N)
        print("missing",missNumber)
        line = stdin.readline().strip()
main()