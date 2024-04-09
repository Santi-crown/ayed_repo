class Node:
    def __init__(self, value = None):
        self.value = None
        self.next = None
        self.setValue(value)
    def setValue(self, value):
        self.value = value
    def setNext(self, next):
        if not (isinstance(next, Node) or next is None):
            raise Exception("The next attribute is not of the expected data type")
        self.next = next
    def __str__(self):
        return "({}) --> {}".format(self.value, self.next if self.next else "X")

myNode = Node('1')
print(myNode)

myNode2 = Node('2')
print(myNode2)

myNode.setNext(myNode2)
print(myNode)
