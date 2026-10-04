class NodeD:
    def __init__(self, val):
        self.val = val
        self.prev_node = None
        self.next_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        new_node = NodeD(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            new_node = NodeD(val)
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next_node = self.head
                self.head.prev_node = new_node
                self.head = new_node
        elif index == self.size:
            self.append(val)
            return
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next_node
            prev = curr.prev_node
            new_node = NodeD(val)
            prev.next_node = new_node
            new_node.prev_node = prev
            new_node.next_node = curr
            curr.prev_node = new_node
        self.size += 1

    def update(self, index, val):
        if index < 0 or index >= self.size:
            raise IndexError()
        curr = self.head
        for _ in range(index):
            curr = curr.next_node
        curr.val = val

    def find(self, val):
        curr = self.head
        idx = 0
        while curr:
            if curr.val == val:
                return idx
            curr = curr.next_node
            idx += 1
        return -1