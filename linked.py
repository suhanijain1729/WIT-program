class Node:
    def __init__(self, value=None, lastn=None, nextn=None):
        self.value = value
        self.lastn = lastn
        self.nextn = nextn
    def __next__(self):
        return self.nextn
class LinkedList:
    def __init__(self):
        self.root = Node()
        self.cur = self.root
    def __len__(self):
        counter = 0
        cur = self.root
        while cur:
            if cur.value is not None:
                counter += 1
            cur = next(cur)
        return counter
    def __iter__(self):
        result = []
        cur = self.root
        while cur:
            result.append(cur.value)
            cur = next(cur)
        return iter(result)
    def push(self, value):
        """Insert value at back"""
        if self.root.value is None:
            self.root.value = value
            return None
        new_node = Node(value, self.cur)
        self.cur.nextn = new_node
        self.cur = new_node
    def pop(self):
        """Remove value at back"""
        if self.root.lastn is None and self.root.nextn is None:
            self.root.value = None
        result = self.cur.value
        self.cur = self.cur.lastn
        return result
    def shift(self):
        """Remove value at front"""
        if self.root.lastn is None and self.root.nextn is None:
            result = self.root.value
            self.root.value = None
            return result
        result = self.root.value
        self.root.nextn.lastn = None
        self.root = self.root.nextn
        return result
    def unshift(self, value):
        """Insert value at front"""
        if self.root.value is None:
            self.root.value = value
            return None
        new_node = Node(value, None, self.root)
        self.root.lastn = new_node
        self.root = new_node
