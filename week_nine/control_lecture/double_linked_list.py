from random import randint
from time import time
from uuid import uuid1

SIZE = int(2e6)

class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self, elements=[]):
        self.head = None
        self.tail = None
        for e in elements:
            self.append(e)

    def append(self, value):
        new_node = Node(value, None, None)
        if self.tail is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = node.prev
                return
            node = node.next

    def remove_duplicates(self):
        values = set()
        node = self.head
        while node is not None:
            if node.value in values:
                next_node = node.next
                self.remove(node.value)
                node = next_node
            else:
                values.add(node.value)
                node = node.next

    def join(self, other):
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
        elif other.head is not None:
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return " <-> ".join(values)

def main():
    ll = LinkedList([1,2,3])
    print("Lista original:", ll)
    ll.append(4)
    print("Lista después de insertar un nuevo elemento:", ll)
    ll.remove(1)
    print("Lista después de eliminar un elemento:", ll)
    ll.append(2)
    ll.append(2)
    print("Lista después de agregar elementos duplicados:", ll)
    ll.remove_duplicates()
    print("Lista después de eliminar elementos duplicados:", ll)
    ll2 = LinkedList([5,6,7])
    ll.join(ll2)
    print("Lista después de unir dos listas:", ll)

main()
