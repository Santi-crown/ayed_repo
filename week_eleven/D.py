# La idea de implementar dos pilas como colas es
# 1. hacer enqueue a las lista 1
# 2. si se quiere hacer dequeue y la lista 2 esta vacía, se pasara todos los elementos de la stack1 a la dos, donde quedaran invertidos+
#   Si no esta vacía, solo se hace pop al stack2
# Ya
stack1 = []
stack2 = []
for i in range(6):
    stack1.append(i+1)
print(stack1)
while stack1:
    stack2.append(stack1.pop())
print(stack2)
print(stack2.pop())
# print(stack1)
# stack1.append(11)
# print(stack1)
# print(stack1.pop())
# print(stack1)
