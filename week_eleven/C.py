# Data structure : stack
from sys import stdin
def is_balanced(u_input):
    openSymbols = []
    for symbol in u_input:
        if symbol in "[(":
            openSymbols.append(symbol)
        elif symbol == ')' and openSymbols and openSymbols[-1] == '(':
            openSymbols.pop()
        elif symbol == ']' and openSymbols and openSymbols[-1] == '[':
            openSymbols.pop()
        else:
            return "No"
    return "No" if openSymbols else "Yes"
# print(balanced)
def main():
    n = int(stdin.readline())
    for i in range(n):
        line = stdin.readline().strip()
        print(is_balanced(line))
main()