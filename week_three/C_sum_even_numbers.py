def sum_even(n):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n % 2 != 0:
        return sum_even(n - 1)
    elif n % 2 == 0:
        return n + sum_even(n-2) # invariante

print(sum_even(9))
