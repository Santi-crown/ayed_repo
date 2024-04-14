# Data structure : stack
from sys import stdin


def is_balanced(u_input):
    openSymbols = []
    closedSymbols = []
    balanced = "Yes"
    for symbol in u_input:
        if symbol in "[(":
            openSymbols.append(symbol)
        elif symbol == ')' and openSymbols and openSymbols[-1] == '(':
            openSymbols.pop()
        elif symbol == ']' and openSymbols and openSymbols[-1] == '[':
            openSymbols.pop()
        else:
            closedSymbols.append(symbol)
    if openSymbols or closedSymbols:
        balanced = "No"
    return balanced
# print(balanced)
def main():
    n = int(stdin.readline())
    for i in range(n):
        line = stdin.readline().strip()
        print(is_balanced(line))
main()