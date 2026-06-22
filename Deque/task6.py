# Задание 7.1.
# Мера сложности у addHead/removeHead и addTail/removeTail будет различаться только у реализации двусторонней очереди на основе массива.
# При такой реализации:
# Добавление элемента в начало очереди (head) будет производиться за O(n) - т.к. необходимо будет пройтись по всем элементам массива и "передвинуть" их;
# Добавление элемента в хвост очереди (tail) будет производиться за амортизированную O(1) если (емкость массива != кол-ву элементов массива), но будет работать за O(n)
# в случае переполнения массива (емкость массива == кол-ву значений массива).

# При реализации двусторонней очереди на основе связанного списка операции addHead/removeHead и addTail/removeTail будут выполняться за O(1).

# Задание 7.2.
class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0
      
    # Асимптотическая сложность O(1)
    def addFront(self, item) -> None:
        new_node = Node(item)
        new_node.next = self.head
        self.len += 1
        
        if self.head is None:
            self.tail = new_node
            self.head = new_node
            return
        
        self.head.prev = new_node
        self.head = new_node
      
    # Асимптотическая сложность O(1)
    def addTail(self, item) -> None:
        new_node = Node(item)
        self.len += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Асимптотическая сложность O(1)
    def removeFront(self):
        if self.head is None:
            return None

        tmp = self.head

        if tmp == self.tail:
            self.tail = tmp.next

        self.head = tmp.next
        if self.head is not None:
            self.head.prev = None
        
        self.len -= 1
        
        return tmp.value
    
    # Асимптотическая сложность O(1)  
    def removeTail(self):
        if self.head is None:
            return None
        
        tmp = self.tail
        self.tail = tmp.prev
        self.len -= 1

        if tmp == self.head:
            self.head = None
        else:
            tmp.prev.next = None
        
        return tmp.value

    def size(self) -> int:
        return self.len
