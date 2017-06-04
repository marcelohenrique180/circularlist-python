from circularlist.dupla.DNode import DNode


class DCircularList:
    def __init__(self):
        self.cursor: DNode = None
        self.size: int = 0

    def add(self, node:DNode):
        if self.cursor is None:
            self.cursor = node
            node.next = node
            node.previous = node
        else:
            node.next = self.cursor.next
            node.previous = self.cursor
            self.cursor.next = node
        self.size = self.size + 1

    def remove(self):
        old_node = self.cursor.next
        self.cursor.next = old_node.next
        self.cursor.next.previous = self.cursor
        old_node.next = None
        old_node.previous = None
        self.size = self.size - 1
        return old_node

    def advance(self):
        self.cursor = self.cursor.next

    def go_back(self):
        self.cursor = self.cursor.previous

    def __str__(self):
        string = "[... "
        for node in range(0, self.size):
            string = string + self.cursor.element + " | "
            self.advance()
        string = string + " ...]"
        return string
