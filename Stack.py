# Sam Cole
# This is the stack class Last in First out

from LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.add_to_end(data)

    def pop(self):
        return self.myList.remove_head()
