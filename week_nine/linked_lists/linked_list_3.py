class Node:
    def __init__(self, value = None):
        self.value = None
        self. next = None
        self.setValue(value)
    def setValue(self,value):
        self.value = value
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setNext(self, node):
        if not (isinstance(node, Node) or node is None):
            raise Exception("The data type of next attribute is not of the expected data type")
        self.next = node
    def __str__(self):
        return "Node({}) --> {}".format(self.value, self.next if self.next else "X")

node1 = Node(1)
node2 = Node(2)
node1.setNext(node2)
print(node1)