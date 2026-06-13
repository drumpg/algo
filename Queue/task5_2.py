# Задание 5.3.
# Асимптотическая оценка O(n) - где n - расстояние на которое нужно передвинуть очередь (в худшем случае двигаем на всю длину очереди).
# Пространственная оценка O(1).
def move_queue(q, step):
    if q.head is None:
        return
    new_tail = q.tail
    new_head = q.head
    q.tail.next = q.head
    for i in range(0, step % q.len):
        new_head = new_head.next
        new_tail = new_tail.next
    
    q.head = new_head
    new_tail.next = None
    q.tail = new_tail

# Рефлексия по заданию 5.3.
# Альтернативным решением может являться создание двух дополнительных массивов для хранения значений до N (arr1) и после N (arr2). Имея два массива мы образуем новую очередь куда запишем сначала значения из arr2, а затем из arr1.
# Альтернативное решение будет иметь асимптотическую сложность O(1), но в худшем случае мы пройдемся по каждому значению дважды, сперва чтобы разделив значения на 2 типа, а затем чтобы добавить их в нужном порядке в результурующий стек. 
# Пространственная оценка альтернативного решения будет O(n) - т.к. мы инициализируем дополнительные ячейки для хранения значений (arr1 и arr2).

# Предложенное мною решение работает только если очередь основана на связанном списке, т.к. замыкает его, запоминает голову и хвост, "прокручивает" очередь на N итераций, отвязывает новый хвост от головы, и обновляет указатели на head и tail. 

# Задание 5.4.
class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.len = 0

    def size(self) -> int:
        return self.len

    def pop(self) -> int:
        if self.head is None:
            return None
        
        tmp = self.head
        self.head = self.head.next
        self.len -= 1
        return tmp.value

    def push(self, value) -> None:
        new_node = Node(value)
        self.len += 1
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def peek(self):
        return self.head.value if self.head is not None else None

class QueueOnStack:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.len = 0

    # Асимптотическая оценка O(1).
    # Пространственнач оценка O(1).
    def enqueue(self, item) -> None:
        self.stack1.push(item)
        self.len += 1

    # Асимптотическая оценка амортизированная O(1) - в случае отсутствия значений в stack2 необходимо пройтись по всему stack1 и переложить значения в stack2 (O(n)), в ином случае O(1).
    # Пространственная оценка O(1).
    def dequeue(self) -> int:
        if self.stack2.peek() is None:
            while self.stack1.peek() is not None:
                self.stack2.push(self.stack1.pop())

        tmp = self.stack2.pop()
        if tmp is not None:
            self.len -= 1
        return tmp

    def size(self) -> int:
        return self.len

# Рефлексия по заданию 5.4.
# Альтернативным решением является реализация очереди не на двух стеках, а на связанном списке или массиве.
# Если не брать в расчет амортизированную асимптотическую O(1), то никакой существенной разницы текущего решения с альтернативой нет.

# Задание 5.5. Работает только для очереди реализованной на связанном списке.
# Асимптотическая оценка O(n) - необходимо пройти по всем элементам очереди.
# Пространственная оценка O(1) - не инициализируем новые сущности.

def reverse(q) -> None:
    previous = None
    curr = q.head
    while curr is not None:
        next = curr.next
        curr.next = previous
        previous = curr
        curr = next

    q.head, q.tail = q.tail, q.head
	
# Рефлексия по заданию 5.5.
# Альтернативным решением является создание массива, в который мы переместим все значения из очереди и затем развернем этот массив и начнем добавлять значения в результирующую очередь.
# Асимптотическая оценка альтернативного решения O(n), у которого тета будет (n+n) - т.к. мы проходим по всем значениям дважды - чтобы заполнить массив и чтобы его развернуть.
# Пространственная оценка альтернативного решения O(n), т.к. мы инициализируем дополнительный массив.

# Задание 5.6.
import ctypes

class Queue:
    def __init__(self) -> None:
        self.capacity = 7
        self.len = 0
        self.head = 0
        self.curr = 0
        self.array = self.__make_array()
            
    def __make_array(self) -> list:
        return (self.capacity * ctypes.py_object)()
    
    # Асимптотическая сложность O(1).
    # Пространственная сложность O(1).
    def enqueue(self, item) -> None:
        if self.is_fill():
            raise IndexError("Array filled")
        
        self.array[self.curr] = item
        self.len += 1
        self.curr = (self.curr + 1) % self.capacity
        
    # Асимптотическая сложность O(1).
    # Пространственная сложность O(1).
    def dequeue(self) -> int:
        if self.len == 0:
            return None
            
        tmp = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.len -= 1
        return tmp

    def size(self) -> int:
        return self.len
    
    def is_fill(self) -> bool:
        return self.len == self.capacity

# Рефлексия по задание 5.6.
# Альтернативным решением может являться реализация очереди на связанном списке.
# При таком решении асимптотическая и пространственная сложности не изменяются, но процессор тратит время на разыменовывание указателей.
