class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_in_tail(self, item) -> None:
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self) -> None:
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Задание 1.1/1.2.
    # Асимптотическяа оценка O(n) - проходим по всем элементам LinkedList и удаляем подходящие. 
    # Пространственная оценка - O(1) - не меняется при входных значениях или от кол-ва элементов в LinkedList.
    def delete(self, val, all=False) -> None:
        new_list = Node(None)
        new_list.next = self.head
         
        curr = self.head
        previous = new_list
        while curr is not None:
            
            if curr.value != val:
                previous = curr
                curr = curr.next
            else:
                previous.next = curr.next
                if curr == self.tail:
                    if previous.value is None:
                        self.tail = None
                    else:
                        self.tail = previous
                    
                del curr
                curr = previous.next
                
                if all != True:
                    break
        self.head = new_list.next
    
    # Задание 1.3. 
    # Асимптотическая оценка O(n) - проходим по всем элементам LinkedList и удаляем их.
    # Пространственная оценка O(1) - не аллоцируем новые данные, а только удаляем.
    def clean(self) -> None:
        node = self.head
        while node is not None:
            tmp = node.next
            del node
            node = tmp
            
        self.head = None
        self.tail = None
        
        
    # Задание 1.4. 
    # Асимптотическая оценка O(n) - проходим по всем элементам LinkedList и записываем подходящие в массив. 
    # Пространственная оценка O(m), где m - кол-во подходящих по значению Node. 
    def find_all(self, val) -> list[Node]:
        res = list()
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    # Задание 1.5. 
    # Асимптотическая оценка O(n) - проходим по всем элементам LinkedList и подсчитываем их кол-во.
    # Пространственная оценка O(1) - инициализируем новую переменную не зависимо от того какое количество элементов содержит LinkedList.
    def len(self) -> int:
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    # Задание 1.6. 
    # Асимптотическая оценка O(n) - в худшем случае проходим по всему LinkedList и вставляем новое значение.
    # Пространственная оценка O(1) - никак не меняется использование памяти по мере роста LinkedList
    def insert(self, afterNode, newNode) -> None:
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    if node == self.tail:
                        self.tail = newNode
                    tmp = node.next
                    newNode.next = tmp
                    node.next = newNode
                    break
                node = node.next
