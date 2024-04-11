from sys import stdin
# throwing cards
# Data structure : queue
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def setValue(self, new_value):
        self.value = new_value
    def getNext(self):
        return self.next
    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")
    def clear(self):
        self.value = None
        self.next = None
    def __str__(self):
        next = self.next
        return "Node("+str(self.value)+") -->" + ("x" if next is None else str(next))

class LinkedList:
    def __init__(self ): # Here we delete values = []
        self.head, self.tail, self.len = None, None, 0
        # Here we delete for e in data, SO WE NEED TO FIX THIS, IT MEAN THAT WE NEED TO APPEND ITERATIVE EACH VALUE OF MY NODES
    def __len__(self):
        return self.len
    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            self.setTail(new_node)
        self.len = self.len + 1
    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    # # Here there is an error cause what if new_tail is not istance of a Node
    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None

    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)

    def slice(self, value, n=1):
        ld = LinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld
    def isEmpty(self):
        return len(self) == 0
    def merge(self, list_b):
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())

    def delete(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1: # Soy el único
                self.head, self.tail = None, None
            else:
                if value_node == self.getHead():
                    self.head = value_node.getNext()
                else:
                    #Buscar el previo a value_node
                    prev = self.head
                    while prev.getNext() != value_node:
                        prev = prev.getNext()
                    if value_node == self.getTail():
                        self.setTail(prev)
                    else:
                        prev.setNext(value_node.getNext())
            value_node.clear()
            self.len -= 1
        else:
            raise Exception("Element not found.")
    # Implementar el método pop para eliminar el primero y devolverlo
    def pop(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else:
            value = self.head.getValue() # Obtener el valor del primer elemento (head)
            self.head = self.head.getNext() # El siguiente nodo se convierte en el nuevo head
            self.len -= 1
            return value
    # Display the linked list as a number list with , between each number
    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current.getValue())
            if current.getNext():
                output += ","
            current = current.getNext()
        return output
# mis funciones
def main():
    # leemos el numero de cartas
    for number in stdin:
        deck_cards = LinkedList()
        ramaining_cards = LinkedList()
        n = int(number.strip())

        for i in range(0, n):
            deck_cards.append(i+1)
        while len(deck_cards) > 1:
            discard_card = deck_cards.pop()
            ramaining_cards.append(discard_card)
            card_not_discard = deck_cards.pop()
            deck_cards.append(card_not_discard)
        remaining_card = deck_cards.head.getValue()
        print("Discarted cards: {} \nRemaining card: {}".format(ramaining_cards, deck_cards.head.getValue()))
main()

