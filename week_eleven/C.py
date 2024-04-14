# Data structure : stack
openSymbols = []
closedSymbols = []
# [] --> "A"
# () --> "P"
# [( --> True
# )] --> False
# Si se intenta sacar algo de una pila que esta vacía, genera underfloor, está mal.
# Para implementar A y P, se puede hacer con un diccionario.
# ([])
balanced = True
u_input = "([])"
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
    balanced = False
# print(openSymbols)
# print(closedSymbols)
print(balanced)
# Casos de aceptación
# openSymbols es vacio

#Casos de no aceptación
# openSymbols no vacio
# Se intentan sacar parentesis de openSymbols vacio - underfloor