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