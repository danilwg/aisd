class NodeS:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        new_node = NodeS(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            new_node = NodeS(val)
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        elif index == self.size:
            self.append(val)
            return
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = NodeS(val)
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def update(self, index, val):
        if index < 0 or index >= self.size:
            raise IndexError()
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = val

    def find(self, val):
        curr = self.head
        idx = 0
        while curr:
            if curr.val == val:
                return idx
            curr = curr.next
            idx += 1
        return -1