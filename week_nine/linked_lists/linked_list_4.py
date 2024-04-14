class Node:
    def __init__(self, value = None):
        self.value = ""
        self.next = None
        self.setValue(value)
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value = value
    def getNext(self):
        return self.next
    def setNext(self, next):
        if not (isinstance(next, Node) or next is None):
            raise Exception("The data type of the next atributte is not of the expected data type")
        self.next = next
    def clear(self):
        self.value = None
        self.next = None
    def __str__(self):
        return "({}) ---> {}".format(self.value, self.next if self.next else "X")
class Linked_list:
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
            raise Exception("El tipo del atributo head no es del tipo de dato esperado.")
        self.head = node
    def setTail(self, node):
        if not isinstance(node, Node):
            raise Exception("El tipo del atributo tail no es del tipo de dato esperado.")
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
    def isEmpty(self):
        return self.head is None
    def find(self, value):
        node_result = self.head
        prev = None
        while node_result is not None and node_result.getValue() != value:
            node_result = node_result.getNext()
        return node_result
    def __str__(self):
        return str(self.head)
    def update(self, old_value, new_value):
        node_to_update = self.find(old_value)
        if node_to_update is not None:
            node_to_update.setValue(new_value)

    def join(self, ll2):
        if not isinstance(ll2, Linked_list):
            raise Exception("El tipo del parametro ll2 no es del tipo de dato esperado.")
        if self.isEmpty():
            return ll2
        if not ll2.isEmpty():
            self.tail.setNext(ll2.head)
            self.tail = ll2.tail
            self.len = len(self) + len(ll2)
        return self
    def delete_by_value(self, value):
        node_to_delete = self.find(value)
        if node_to_delete is not None:
            if len(self) == 1: # I'm the only one
                self.head, self.tail = None, None
            else:
                if node_to_delete == self.head:
                    self.head = node_to_delete.getNext()
                else:
                    #Bucar el previo a node_to_delete
                    prev = self.head
                    while prev.getNext() != node_to_delete:
                        prev = prev.getNext()
                    if node_to_delete == self.tail:
                        self.setTail(prev)
                    else:
                        prev.setNext(node_to_delete.getNext())
            node_to_delete.clear()
        else:
            raise Exception("Element not found")
def main():
    # ll = Linked_list([1,2,3,4,5,6,7,8,9,10])
    # print(ll)
    # print(ll.find(10))
    # print("Updating a value")
    # ll.update(5, 5.1)
    # print(ll)
    ll = Linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ll2 = Linked_list([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    print(ll)
    print(ll2)
    ll.join(ll2)
    print(ll)
    ll.delete_by_value(6)
    print(ll)

main()