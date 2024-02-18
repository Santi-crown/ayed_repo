from sys import stdin

def binary(n):                                          # costo   pasos
    if n // 2 == 0:                                     #   1       1
        return [n % 2]                                  #   1       1
    return [n % 2] + binary(n // 2) # invariante        #   n       n
                                                        # Total O = (n)
n = stdin.readline().strip()

while n != '':
    binary_list = binary(int(n))
    binary_list.reverse()
    # print each list of binary as a string concatenates
    print(''.join(map(str,binary_list)))
    n = stdin.readline().strip()