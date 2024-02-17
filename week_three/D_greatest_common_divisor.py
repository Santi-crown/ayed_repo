from sys import stdin

def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m % n) # invariante

# print(gcd(100,95))

inputs = stdin.readline().strip().split()
int_inputs = list(map(int,inputs))

n,m = int_inputs[0], int_inputs[1]

print(gcd(n,m))