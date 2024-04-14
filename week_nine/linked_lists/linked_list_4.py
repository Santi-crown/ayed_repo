class Node:
    def __init__(self, value = None):
        self.value = ""
        self.next = None
        self.setValue(value)
    def getValue(self):
        return self.value
    def setValue(self,value):
        if not isinstance(value, str):
            raise Exception("The value is not of the data type expected")
        self.value = value
    def getNext(self):
        return self.next
    def setNext(self, next):
        if not (isinstance(next, Node) or None):
            raise Exception("The data type of the next atributte is not of the expected data type")
        self.next = next
    def __str__(self):
        return "({}) ---> {}".format(self.value, self.next if self.next else "X")

node1 = Node('1')
node2 = Node('2')
node1.setNext(node2)
print(node1)

class linked_list:
    def __init__(self, values = []):
        self.head = None
        self.tail = None