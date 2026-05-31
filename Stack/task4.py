# Задание 4.1
# class Node:
#     def __init__(self, value) -> None:
#         self.val = value
#         self.next = None
#         self.prev = None
        
# class LinkedList():
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None

# class Stack:
#     def __init__(self) -> None:
#         self.stack = LinkedList()
#         self.len = 0

#     def size(self) -> int:
#         return self.len

#     # Асимптотическая сложность O(1) - за счет использования двусвязного списка.
#     # Пространственная сложность O(1)
#     def pop(self) -> int:
#         if self.size() == 0:
#             return None
        
#         tmp = self.stack.tail
#         self.stack.tail = self.stack.tail.prev
#         self.len -= 1

#         if tmp.prev != None:
#             tmp.prev.next = None
        
#         if tmp == self.stack.head:
#             self.stack.head = self.stack.tail
        
#         return tmp.val

#     # Асимптотическая сложность O(1)
#     # Пространственная сложность O(1)
#     def push(self, value) -> None:
#         node = Node(value)
#         if self.stack.head == None:
#             self.stack.head = node
#             self.stack.tail = node
#         else:
#             node.prev = self.stack.tail
#             self.stack.tail.next = node
#             self.stack.tail = node
            
#         self.len += 1

#     def peek(self):
#         return self.stack.tail.val if self.size() > 0 else None

# Задание 4.2
class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.stack = None
        self.len = 0

    def size(self) -> int:
        return self.len

    # Асимптотическая сложность O(1)
    # Пространственная сложность O(1)
    def pop(self) -> int:
        if self.size() == 0:
            return None
        
        tmp = self.stack
        self.stack = self.stack.next
        self.len -= 1
        return tmp.val

    # Асимптотическая сложность O(1)
    # Пространственная сложность O(1)
    def push(self, value) -> None:
        node = Node(value)
        node.next = self.stack
        self.stack = node
        self.len += 1

    def peek(self):
        return self.stack.val if self.size() > 0 else None

# Задание 4.3
# Пока в стеке есть элементы мы за одну итерацию цикла будем удалять по 2 элемента. Получая при этом элементы с конца (Last in). Например в стеке со значениями [1, 2, 3] мы увидим следующий вывод:
# 3
# 2
# 1
# None
