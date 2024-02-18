from sys import stdin

def gcd(m,n):                                   # costo   pasos
    if n == 0:                                  #   1       1
        return m                                #   1       1
    return gcd(n,m % n) # invariante            #   n       n
                                                # Total O = (n)
# print(gcd(100,95))
# print(gcd(100,95))
inputs = stdin.readline().strip().split()

while len(inputs) > 0:
    int_inputs = list(map(int,inputs))
    n,m = int_inputs[0], int_inputs[1]
    print(gcd(n,m))
    inputs = stdin.readline().strip().split()