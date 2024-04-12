from collections import deque

myStack = deque()

myStack.append('1')
myStack.append('2')
myStack.append('3')
myStack.append('4')
print(myStack)
pop_element = myStack.pop()
print(myStack)
# LIFO - STACK
print(pop_element)
myStack.append('4')
print(myStack)
# FIFO -  QUEUE
print(myStack[-2])


