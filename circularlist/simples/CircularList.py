from circularlist.simples.Node import Node


class CircularList:
    def __init__(self):
        self.cursor: Node = None
        self.size: int = 0

    def add(self, node):
        if self.cursor is None:
            self.cursor = node
            node.next = node
        else:
            node.next = self.cursor.next
            self.cursor.next = node
        self.size = self.size + 1

    def remove(self):
        old_node = self.cursor.next
        self.cursor.next = old_node.next
        old_node.next = None
        self.size = self.size - 1
        return old_node

    def advance(self):
        self.cursor = self.cursor.next

    def __str__(self):
        string = "[... "
        for node in range(0, self.size):
            string = string + self.cursor.element + " | "
            self.advance()
        string = string + " ...]"
        return string
