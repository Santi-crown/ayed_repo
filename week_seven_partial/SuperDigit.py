# import sys
#
#
# def super_digit(n):
#     if len(n) == 1:
#         return n
#     return super_digit(str(sum(map(int,n))))
#
# def super_digitP(n,M = {}):
#     if len(n) == 1:
#         return n
#     return super_digit(str(sum(map(int,n))),M)
#
# def super_digitMemo(n,k,M = {}):
#     if (n,k) in M.keys():
#         return M[n,k]
#     M[n,k] = super_digitP(n,k,M)
#     return M[(n,k)]
#
# def main():
#     for line in sys.stdin:
#         n,k = line.split()
#         n = str(sum(map(int,n))* int(k))
#         print(super_digit(n))
# main()

# try 1
# import sys
#
# def super_digit(n):
#     if len(n) == 1:
#         return n
#     return super_digit(str(sum(map(int,n))))
#
# def super_digitP(n, M = {}):
#     if len(n) == 1:
#         return n
#     return super_digitMemo(str(sum(map(int,n))),M)
#
# def super_digitMemo(n,k,M = {}):
#     if (n,k) in M.keys():
#         return M[(n,k)]
#     M[(n, k)] = super_digitP(n,k,M)
#     return M[(n, k)]
#
# def main():
#     for line in sys.stdin:
#         n,k = line.split()
#         n = str(sum(map(int,n))* int(k))
#         print(super_digit(n))
# main()

# try 2
import sys
def super_digit(n):
    if len(n) == 1:
        return n
    return super_digit(str(sum(map(int,n))))

def super_digitP(n,M = {}):
    if len(n) == 1:
        return n
    return super_digit(str(sum(map(int,n))),M)

def super_digitMemo(n,k,M={}):
    if (n,k) in M.keys():
        return M[(n,k)]
    M[(n, k)] = super_digitP(n,k,M)
    return M[(n,k)]

def main():
    for lines in sys.stdin:
        n,k = lines.split()
        n = str(sum(map(int,n))*int(k))
        print(super_digit(n))
main()