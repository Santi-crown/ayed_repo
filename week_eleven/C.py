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
underFloor = False
balanced = False
u_input = "(([()])))"
for symbol in u_input:
    if symbol == '(' or symbol == '[':
        openSymbols.append(symbol)
    elif symbol == ')' and len(openSymbols) > 0 and openSymbols[-1] == '(':
        try:
            openSymbols.pop()
        except IndexError:
            underFloor = True
            print("WTF BROU")
    elif symbol == ']'  and len(openSymbols) > 0 and openSymbols[-1] == '[':
        try:
            openSymbols.pop()
        except IndexError:
            underFloor = True
if len(openSymbols) == 0 and underFloor is False:
    balanced = True
print(balanced)
