def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m % n) # invariante

print(gcd(100,95))