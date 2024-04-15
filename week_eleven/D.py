# La idea de implementar dos pilas como colas es
# 1. hacer enqueue a las lista 1
# 2. si se quiere hacer dequeue y la lista 2 esta vacía, se pasara todos los elementos de la stack1 a la dos, donde quedaran invertidos+
#   Si no esta vacía, solo se hace pop al stack2
# Ya
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, values):
        self.stack1.append(values)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()
    def peek(self):
        if self.stack1:
            return self.stack1[0]
        elif self.stack2:
            return self.stack2[-1]
        else:
            return None #Caso que ambas están vacias.
    def __str__(self):
        return str(self.stack1)

myQueue = QueueWithTwoStacks()

myQueue.enqueue(42)
myQueue.dequeue()
myQueue.enqueue(14)
print(myQueue.peek())
myQueue.enqueue(28)
print(myQueue.peek())
myQueue.enqueue(60)
myQueue.enqueue(78)
myQueue.dequeue()
myQueue.dequeue()
#print(myQueue)




