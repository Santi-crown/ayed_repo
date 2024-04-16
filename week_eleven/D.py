from sys import stdin
# La idea de implementar dos pilas como colas es
# 1. hacer enqueue a las lista 1
# 2. si se quiere hacer dequeue y la lista 2 esta vacía, se pasara todos los elementos de la stack1 a la dos, donde quedaran invertidos+
#   Si no esta vacía, solo se hace pop al stack2
# Ya
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def put(self, values):
        self.stack1.append(values)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()
    def peek(self):
        if not self.stack2:
           while self.stack1:
               self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def __str__(self):
        return str(self.stack1)
def main():
    myQueue = QueueWithTwoStacks()
    q = int(stdin.readline().strip())
    # 1 restriction
    if q >= 0 and q <= 10**5:
        for query in range(q):
            line = stdin.readline().split()
            type = line[0]
            # 2 restriction
            if type == '1':
                value = line[1]
                # 3 restriction
                if int(value) >= 0 and int(value) <= 10**9:
                    myQueue.put(value)
                #print(type, value)
            elif type == '2':
                myQueue.pop()
            elif type == '3':
                print(myQueue.peek())
main()




