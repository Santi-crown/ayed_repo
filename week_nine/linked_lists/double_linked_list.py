class Node:
    def __init__(self, value = None):
        self.value = ""
        self.next = None
        self.prev = None
        self.setValue(value)
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def getNext(self):
        return self.next
    def setNext(self, node):
        if not isinstance(node, Node):
            raise Exception("Next is not a node")
        self.next = node
    def getPrev(self):
        return self.prev
    def setPrev(self, node):
        if not isinstance(node, Node):
            raise Exception("Prev is not a node")
        self.prev = node
    def __str__(self):
        return "({}) ---> {}".format(self.value, self.next if self.next else "X")

    def clear(self):
        self.value = None
        self.next = None
        self.prev = None
class Double_linked_list:
    def __init__(self, values = []):
        self.head = None
        self.tail = None
        self.len = 0
        for e in values:
            self.append(e)
    def __len__(self):
        return self.len
    def setHead(self, node):
        if not isinstance(node, Node):
            raise Exception("El tipo del atributo head no es del tipo de dato esperado.")
        self.head = node

    def setTail(self, node):
        if not isinstance(node, Node):
            raise Exception("El tipo del atributo tail no es del tipo de dato esperado.")
        self.tail = node
        if self.tail is not None:
            self.tail.setNext(None)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node2.setPrev(node1)
node2.setNext(node3)
print(node2)