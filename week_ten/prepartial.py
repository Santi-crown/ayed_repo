class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "({}) --> {}".format(self.data, self.next if self.next else "X")
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def __str__(self):
        return str(self.head)
    # def display(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")
# Ejemplo de uso
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(ll)  # Salida: 1 -> 2 -> 3 -> None

# Casos
ll.delete(2)
print(ll)  # Salida: 1 -> 3 -> None
print(ll.search(3))  # Salida: True
print(ll.search(5))  # Salida: False
