class DNode:
    def __init__(self, element, next_node=None, prev_node=None):
        self.element = element
        self.next: DNode = next_node
        self.previous: DNode = prev_node
