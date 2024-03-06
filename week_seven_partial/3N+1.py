# from sys import stdin
#
# memo = {}
#
# def numTNOne(n):   # Función que describe 3N + 1 en general
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOne(n//2)
#     return 1 + numTNOne(3*n+1)
#
# def numTNOneP(n,M): # Función que servirá de soporte para almacenar información y despues guardarlo en memoria
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOneMemo (n//2,M)
#     return 1 + numTNOneMemo(3 * n + 1, M)
#
# def numTNOneMemo(n,M): # Función memoria
#     if n in M.keys():
#         return M[n]
#     M[n] = numTNOneP(n,M)
#     return M[n]
#
# def map_numTNOneMemo(n):    #Función que recurrirá a guardar los datos en la memo, que se creó como diccionario
#     if n in memo.keys():
#         return memo[n]
#     memo[n] = numTNOneP(n,memo)
#     return memo[n]
#
# def maxNumTNOne(n,m):    #Retorna el máximo valor de hacer los cáculos del número n y m
#     return max(map(map_numTNOneMemo, range(n,m+1)))
#
# def main():
#     line = stdin.readline().strip()
#     while line:
#         n,m = map(int,line.split())
#         print(n,m, maxNumTNOne(min(n,m),max(n,m)))
#         line = stdin.readline().strip()
# main()

# try 1

# from sys import stdin
# memo = {}
# def numTNOne(n):                         #Función que describe de forma general 3N + 1
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         1 + numTNOne(n // 2)
#     return 1 + numTNOne(3 * n + 1)
#
# def numTNOneP(n,M):                     #Función que servira de soporte para almacenar información y despues guardarla en la memoria
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOneMemo(n//2, M)
#     return 1 + numTNOneMemo(3 * n + 1, M)
#
# def numTNOneMemo(n,M):                  #Función memoria
#     if n in M.keys():
#         return M[n]
#     M[n] = numTNOneP(n,M)
#     return M[n]
#
# def map_numTOnesMemo(n):               #Función que recurrirá a guardar los datos en memo que se creo como diccionario
#     if n in memo.keys():
#         return memo[n]
#     memo[n] = numTNOneP(n,memo)
#     return memo[n]
#
# def maxNumTNOne(n,m):
#     return max(map(map_numTOnesMemo, range(n,m+1))) #Retorna el máximo valor de hacer los cáculos del número n y m
#
# def main():
#     line = stdin.readline().strip()
#     while line:
#         n,m = map(int, line.split())
#         print(n,m,maxNumTNOne(min(n,m),max(n,m)))
#         line = stdin.readline().strip()
# main()

# Try 2
# from sys import stdin
# memo = {}
#
# def numTNOne(n):                       # Definición general
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         1 + numTNOne(n//2)
#     return 1 + numTNOne(3 * n + 1)
#
# def numTNOneP(n,M):                      # Me ayuda de soporte para almacenar y luego guardar en memoria
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOneMemo(n//2,M)
#     return 1 + numTNOneMemo(3 * n + 1, M)
#
# def numTNOneMemo(n,M):                  # Función memoria
#     if n in M.keys():
#         return M[n]
#     M[n] = numTNOneP(n,M)
#     return M[n]
#
# def map_numTNOneMemo(n):                # Guardamos los datos en memoria
#     if n in memo.keys():
#         return memo[n]
#     memo[n] = numTNOneP(n,memo)
#     return memo[n]
#
# def maxNumTNOne(n,m):                   # Retornamos el máximo valor de los cálculos.
#     return max(map(map_numTNOneMemo, range(n,m+1)))
#
# def main():
#     line = stdin.readline().strip()
#     while line:
#         n, m = map(int, line.split())
#         print(n, m, maxNumTNOne(min(n, n), max(n, m)))
#         line = stdin.readline().strip()
# main()

#try 3
# from sys import stdin
# # 1. Definición general
# # 2. F prima
# # 3. F memo
# # 4. F map_memo
# # 5. F max calculos
# # 6. main
# memo = {}
#
# def numTNOne(n):
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOne(n//2)
#     return 1 + numTNOne(3 * n + 1)
#
# def numTNOneP(n,M):
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return 1 + numTNOneMemo(n//2,M)
#     return 1 + numTNOneMemo(3 * n + 1, M)
#
# def numTNOneMemo(n,M):
#     if n in M.keys():
#         return M[n]
#     M[n] = numTNOneP(n,M)
#     return M[n]
#
# def map_numTNOneMemo(n):
#     if n in memo.keys():
#         return memo[n]
#     memo[n] = numTNOneP(n, memo)
#     return memo[n]
#
# def maxNumTNOne(n,M):
#     return max(map(map_numTNOneMemo,range(n,M+1)))
#
# def main():
#     line = stdin.readline().strip()
#     while line:
#         n,m = map(int,line.split())
#         print(n,m,maxNumTNOne(min(n,m),max(n,m)))
#         line = stdin.readline().strip()
#
# main()

# try 4
from sys import stdin
memo = {}
#1. f general
#2. f prima
#3. f memo
#4. f map_memo
#5. f max num
#6. main

def numTNOne(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return 1 + numTNOne(n//2)
    return 1 * numTNOne(3 * n + 1)
def numTNOneP(n, M):
    if n == 1:
        return 1
    if n%2 == 0:
        return 1 + numTNOneMemo(n//2,M)
    return 1 * numTNOneMemo(3 * n + 1,M)
def numTNOneMemo(n,M):
    if n in M.keys():
        return M[n]
    M[n] = numTNOneP(n,M)
    return M[n]
def map_numTNOneMemo(n):
    if n in memo.keys():
        return memo[n]
    memo[n] = numTNOneP(n, memo)
    return memo[n]
def maxNumTNOne(n,M):
    return max(map(map_numTNOneMemo,range(n,M+1)))
def main():
    line = stdin.readline().strip()
    while line:
        n,m = map(int,line.split())
        print(n,m, maxNumTNOne(min(n,m),max(n,m)))
        line = stdin.readline().strip()
main()
# try 5

# try 6

































