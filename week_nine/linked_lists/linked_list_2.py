class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = None
        self.setValue(value)
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setNext(self, next):
        if not (isinstance(next, Node) or next is None):
            raise Exception("The type of the next attribute is not of the expected data type")
        self.next = next
    def __str__(self):
        return "Node({}) --> {}".format(self.value, self.next if self.next else 'X')
class LinkedList:
    def __init__(self, elements = []):
        self.head = None
        self.tail = None
        self.len = 0
        for e in elements:
            self.append(e)
    def __len__(self):
        return self.len
    def setHead(self, node):
        if not isinstance(node, Node):
            raise Exception("The type of the attribute head is not of the expected data type")
        self.head = node
    def setTail(self, node):
        if not isinstance(node, Node):
            raise Exception("The type of the attribute tail is not of the expected data type")
        self.tail = node
        if self.tail is not None:
            self.tail.setNext(None)
    def append(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.setHead(new_node)
            self.setTail(new_node)
        else:
            tail = self.tail
            tail.setNext(new_node)
            self.setTail(new_node)
        self.len += 1
    def find(self, value):
        node_result = self.head
        while node_result is not None and node_result.getValue() != value:
            node_result = node_result.getNext()
        return node_result
    def update(self, old_value, new_value):
        node_to_update = self.find(old_value)
        if node_to_update is not None:
            node_to_update.setValue(new_value)
    def isEmpty(self):
        return self.head is None
    def __str__(self):
        return str(self.head)
    def join(self, ll2):
        if not isinstance(ll2, LinkedList):
            raise Exception("The type of the parameter ll2 is not fo the expected data type")
        if self.isEmpty():
            return ll2
        if not ll2.isEmpty():
            self.tail.setNext(ll2.head)
            self.tail = ll2.tail
            self.len = self.len + len(ll2)
def main():
    myLinkedList = LinkedList(['Harry','Hermione','Ron'])
    print(myLinkedList)
main()






