from sys import stdin

def write(line):
    words = []
    index = 0
    for i in line:
        if len(i) > index:
            words.append(i[index])
            index += 1
    words = map(str, words)
    print("".join(words))
    return index

def main():
    rango = int(stdin.readline().strip())
    empty = stdin.readline()
    for i in range(rango):
        print("Case #" + str(i + 1) + ":")
        line = stdin.readline().strip().split(" ")
        # print(line)
        while len(line[0]) > 0:
            write(line)
            line = stdin.readline().strip().split(" ")
            # print(line)
main()