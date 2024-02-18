from sys import stdin

def sum_even(n):                                    # costo   pasos
    if n < 2:                                       #   1       1
        return 0                                    #   1       1
    elif n == 2:                                    #   1       1
        return 2                                    #   1       1
    elif n % 2 != 0:                                #   1       1
        return sum_even(n - 1)                      #   1       1
    elif n % 2 == 0:                                #   1       1
        return n + sum_even(n-2) # invariante       #   n       n
                                                    # Total O = (n), omega = 1
n = stdin.readline().strip()

while n != '':
    print(sum_even(int(n)))
    n = stdin.readline().strip()

