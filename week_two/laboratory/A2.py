# coding: utf-8
from sys import stdin

def write(line):  # costo pasos
    words = []  # 1 1
    index = 0  # 1 1
    for i in line:  # Ciclo de la invariante #1 # 1 n
        if len(i) > index:  # 1 n - 1
            words.append(i[index])  # 1 n - 1
            index += 1  # 1 n - 1
    words = map(str, words)  # 1 1
    print("".join(words))  # 1 1
    return index  # 1 1
    # Total O = (n), omega = 1

def main():  # costo pasos
    rango = int(stdin.readline().strip())  # 1 1
    for i in range(rango):  # Ciclo de la invariante #1 # 1 j
        print("Case #" + str(i + 1) + ":")  # 1 j-1
        line = stdin.readline().strip().split(" ")  # 1 j-1
        while len(line[0]) > 0:  # 1 j-1
            write(line)  # write(n) j-1
            line = stdin.readline().strip().split(" ")  # 1 j-1

if __name__ == '__main__':  # Total O = (jn+j) omega = 1
    main()
