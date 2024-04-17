from sys import stdin
def is_balanced(symbols):
    open_parentheses = []
    for symbol in symbols:
        if symbol in '([':
            open_parentheses.append(symbol)
        elif symbol == ')' and open_parentheses and open_parentheses[-1] == '(':
            open_parentheses.pop()
        elif symbol == ']' and open_parentheses and open_parentheses[-1] == '[':
            open_parentheses.pop()
        else:
            return "No"
    return 'No' if open_parentheses else "yes"

def main():
    n = int(stdin.readline().strip())
    for line in range(n):
        symbols = stdin.readline().strip()
        answer = is_balanced(symbols)
        print(answer)
main()


