#链表中间节点的删除
class DNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = DNode(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = DNode(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_node(self, index):
        if index <= self.size // 2:
            current = self.head
            for i in range(index - 1):
                current = current.next
        else:
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        return current

    def insert(self, data, index):
        new_node = DNode(data)
        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        else:
            current = self.get_node(index)
            current.next.prev = new_node
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current=self.get_node(index)
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1

    def __getitem__(self,index):
        if index == 0:
            return self.head.data
        elif index == self.size:
            return self.tail.data
        else:
            current = self.get_node(index)
            return current.data

    def __len__(self):
        return self.size



