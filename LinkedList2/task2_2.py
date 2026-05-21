# Задание 2.10.
# Разворот LinkedList.
# Асимптотическая оценка O(n) - мы проходим по каждому элементу LinkedList и меняем указатели "next" и "prev" местами.
# Пространственная оценка O(1) - количество создаваемых объектов не растет от количества элементов в LinkedList.
    def reverse(self) -> None:
        prev = None
        curr = self.head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            curr.prev = tmp
            
            prev = curr
            curr = tmp
            
        self.head, self.tail = self.tail, self.head
   
# Рефлексия по 2.10.
# Альтернативным решением может быть создание 
нового LinkedList. В таком решении мы будем идти с конца (tail) до начала (head), параллельно добавляя ноды в новый LinkedList.
# Асимптотическая оценка O(n) - не изменяется.
# Пространственная оценка O(n) - т.к. создается дополнительный "развернутый" LinkedList.

# Задание 2.11.
# Проверка LinkidList на цикличность.
# Асимптотическая оценка O(n) - необходимо пройти по всему LinkedList.
# Пространственная оценка O(1) - не менятся в зависимости от количества элементов в LinkedList.
    def is_loop(self) -> bool:
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

# Рефлексия по 2.11.
# Альтернативным решением является заполнение множества пройденными нодами. Необходимо создать множество и итерироваться по LinkedList, на каждой итерации заносить node в множество. При таком решении, если добавляемая node уже есть во множестве, то LinkedList цикличен.
# Асимптотическая оценка O(n) - необходимо пройти по всем элементам LinkedList.
# Пространственная оценка O(n) - т.к. создаем дополнительное хранилище уникальных node. 

# Задание 2.12.
# Сортировка LinkedList.
# Асимптотическая оценка O(n^2) - проходим по всему LinkedList n раз.
# Пространственная оценка O(1) - не инициализируем новые сущности.
    def sort(self) -> None:
        for i in range(self.len()):
            prev = self.head
            curr = self.head.next
            while curr is not None:
                if prev.value > curr.value:
                    curr.value, prev.value = prev.value, curr.value
                prev = prev.next
                curr = curr.next

# Рефлексия по 2.12.
# Альтернативным решением может создание дополнительного
    
    import copy
    def merge(self, second_list):
        self.sort()
        second_list.sort()
        node1 = self.head
        node2 = second_list.head
        res = LinkedList2()
        while node1 is not None and node2 is not None:
            if node1.value > node2.value:
                res.add_in_tail(copy.copy(node2))
                node2 = node2.next
            else:
                res.add_in_tail(copy.copy(node1))
                node1 = node1.next
        tail = node1 or node2
        while tail is not None:
            res.add_in_tail(tail)
            tail = tail.next
        return res
        

