# Задания 5.1 - 5.2
class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    # Асимптотическая оценка O(1)
    # Пространственная оценка O(1)
    def enqueue(self, item) -> None:
        new_node = Node(item)
        self.len += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # Асимптотическая оценка O(1)
    # Пространственная оценка O(1)
    def dequeue(self) -> int:
        if self.head is None:
            return None

        tmp = self.head
        self.head = self.head.next
        self.len -= 1
        
        if tmp == self.tail:
            self.tail = None
        
        return tmp.value

    def size(self) -> int:
        return self.len
