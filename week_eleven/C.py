# Data structure : stack
from collections import deque
openSymbols = deque()
# [] --> "A"
# () --> "P"
# [( --> True
# )] --> False
# Si se intenta sacar algo de una pila que esta vacía, genera underfloor, está mal.
# Para implementar A y P, se puede hacer con un diccionario.
# ([])
u_input = "(([()])))"
for symbol in u_input:
    if symbol == '(' or symbol == '[':
        openSymbols.append(symbol)
    elif symbol == ')' and openSymbols[-1] == '(':
        openSymbols.pop()
    elif symbol == ']' and openSymbols[-1] == '[':
        openSymbols.pop()
if len(openSymbols) == 0:
    print(True)
else:
    print(False)
    # print(openSymbols)
    # print(openSymbols)

