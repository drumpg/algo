# Задание 7.3.
# Асимптотическая оценка O(n) - проходим по всем значениям деки.
# Пространственная оценка O(n) - создаем деку размером с n, где n - кол-во элементов в выражении.
def is_pallindrome(expression) -> bool:
    dq = Deque()
    for v in expression:
        dq.addTail(v)

    while dq.head is not None:
        head_elem = dq.removeFront()
        tail_elem = dq.removeTail()
        if head_elem != tail_elem:
            return tail_elem is None
    
    return True

# Рефлексия по заданию 7.3.
# Альтернативным решением является использование двух указателей.
# При таком решении мы идем с начала строки и с конца одновременно, направляясь к середине строки.
# На каждой итерации сравниваем левоей значение с правым, если значения не равны, то возвращаем False.
# Асимптотическая оценка альтернативного решения O(n) - т.к. проходим по всем элементам строки.
# Пространственная оценка альтернативного решения O(1) - т.к. не создаем дополнительных структур для хранения элементов строки.

# Задание 7.4.
# Асимптотическая оценка O(1).
# Пространственная оценка O(N).
class DequeWithMin:
    def __init__(self):
        self.left = Deque()
        self.right = Deque()

    def addFront(self, item):
        if self.left.size() == 0:
            self.left.addFront((item, item))
            return
        
        self.left.addFront((item, min(item, self.left.head.value[1])))

    def addTail(self, item):
        if self.right.size() == 0:
            self.right.addFront((item, item))
            return
        
        self.right.addFront((item, min(item, self.right.head.value[1])))

    def removeFront(self):
        if self.size() == 0:
            return None
        
        if self.left.size() > 0:
            return self.left.removeFront()[0]
        
        self.__shift(self.right, self.left)
        return self.left.removeFront()[0]

    def removeTail(self):
        if self.size() == 0:
            return None
        
        if self.right.size() > 0:
            return self.right.removeFront()[0]

        self.__shift(self.left, self.right)
        return self.right.removeFront()[0]

    def size(self):
        return self.left.size() + self.right.size()

    def get_min(self):
        if self.size() == 0:
            return None
        
        left_min = self.left.head.value[1] if self.left.size() > 0 else float('inf')
        right_min = self.right.head.value[1] if self.right.size() > 0 else float('inf')
        return min(left_min, right_min)

    def __shift(self, source, target):
        while source.size() > 0:
            val, _ = source.removeFront()
            if target.size() == 0:
                target.addFront((val, val))
            else:
                target.addFront((val, min(val, target.head.value[1])))

# Рефлексия по заданию 7.4.
# Альтернативным решением может быть использование стека вместо деки, для избежания излишней логики по работе с двумя выходами и входами.
# При альтернативном решении асимптотическая и пространственная сложности не изменяются.

# Задание 7.5.
# Асимптотическая оценка амортизированная O(1) - т.к. в редком случае придется увеличивать или уменьшать емкость масссива, что занимает O(n).
import ctypes
class Deque:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.__make_array(self.capacity)
        self.head = int(self.capacity / 2)
        self.tail = int(self.capacity / 2)

    def addFront(self, itm) -> None:
        if self.head == 0:
            self.__resize(2 * self.capacity)
        
        self.array[self.head-1] = itm
        self.count += 1
        self.head -= 1
      
    def addTail(self, itm) -> None:
        if self.tail == self.capacity:
            self.__resize(2 * self.capacity)

        self.array[self.tail] = itm
        self.count += 1
        self.tail += 1

    def removeFront(self):
        tmp = self.array[self.head]
        
        self.array[self.head] = None
        self.count -= 1
        self.head += 1
        self.__realloc()

        return tmp

    def removeTail(self):
        tmp = self.array[self.tail-1]

        self.array[self.tail-1] = None
        self.count -= 1
        self.tail -= 1
        self.__realloc()

        return tmp

    def size(self) -> int:
        return self.count

    def __make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __resize(self, new_capacity) -> None:
        new_array = self.__make_array(new_capacity)
        new_head = int((new_capacity - self.count) / 2)
        new_tail = new_head + self.count

        for i in range(self.count):
            new_array[i+new_head] = self.array[self.head+i]

        self.array = new_array
        self.capacity = new_capacity
        self.head = new_head
        self.tail = new_tail
    
    def __realloc(self) -> None:
        ratio = int((self.count / self.capacity) * 100)
        new_cap = int(self.capacity / 1.5)
        if ratio < 40 and self.capacity > 16:
            self.__resize(max(new_cap, 16))

# Рефлексия по заданию 7.5.
# Идея реализации деки на основе динамического массива - заключается в изменении логики добавления элементов.
# При заполнении массива мы начинаем заполнять его с середины, таким образом оставляя равное кол-во "свободного" места для заполнения через head и tail.

# Альтернативным решением является реализация на основе связанного списка, в таком случае мы избавляемся от необходимости уменьшать или расширять емкость Deque.
# Таким образом альтернативное решение работает за O(1) по времени как на удаление (в голову/хвост), так и на добавление (в голову/хвост).

# Задание 7.6.
# Асимптотическая оценка O(n) - проходим по каждому элементу выражение.
# Пространственная оценка O(m) - создаем деку размера m, где m - кол-во открывающихся скобок в выражении.
def is_balanced(string) -> bool:
    dq = Deque()
    pair = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for char in string:
        if char in pair.keys():
            dq.addFront(char)

        if char in pair.values() and dq.size() == 0:
            return False

        if char in pair.values():
            if (pair[dq.head.value] == char):
                dq.removeFront()
            else:
                return False
            
    return dq.size() == 0

# Рефлексия по 7.6.
# Альтернативным решением является использование словаря с подсчетом открывающих и закрывающих скобок.
# Если открывающие скобки != закрывающим скобкам, то возвращаем False.
# Асимптотическая и пространственная оценки при альтернативном решении не изменяются.
