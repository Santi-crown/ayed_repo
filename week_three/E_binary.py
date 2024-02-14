def binary(n):
    if n // 2 == 0:
        return [n % 2]
    return [n % 2] + binary(n // 2) # invariante

print(binary(5))