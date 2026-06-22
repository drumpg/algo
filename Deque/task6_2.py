import unittest
from task6 import Deque

class TestDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.dq = Deque()
        
    def test_addFront(self) -> None:
        self.assertListEqual(self.comparable(self.dq), []) # Проверка значений пустой деки
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)
        
        self.dq.addFront(3) # Добавление элемента в пустую деку
        self.assertEqual(self.dq.head.value, 3)
        self.assertEqual(self.dq.tail.value, 3)

        self.dq.addFront(4) # Добавление нескольких значений в деку
        self.dq.addFront(5)
        self.dq.addFront(6)
        self.assertListEqual(self.comparable(self.dq), [6, 5, 4, 3])
        self.assertEqual(self.dq.head.value, 6)
        self.assertEqual(self.dq.tail.value, 3)

    def test_addTail(self) -> None:
        self.dq.addTail(3) # Добавление элемента в пустую деку
        self.assertEqual(self.dq.head.value, 3)
        self.assertEqual(self.dq.tail.value, 3)

        self.dq.addTail(4) # Добавление нескольких значений в деку
        self.dq.addTail(5)
        self.dq.addTail(6)
        self.assertListEqual(self.comparable(self.dq), [3, 4, 5, 6])
        self.assertEqual(self.dq.head.value, 3)
        self.assertEqual(self.dq.tail.value, 6)

    def test_removeFront(self) -> None:
        self.dq.addTail(1)
        self.dq.addTail(2)
        self.dq.addTail(3)
        
        self.assertEqual(self.dq.removeFront(), 1) # Удаление элемента из деки
        self.assertListEqual(self.comparable(self.dq), [2, 3])
        self.assertEqual(self.dq.head.value, 2)
        self.assertEqual(self.dq.tail.value, 3)

        self.assertEqual(self.dq.removeFront(), 2) # Удаление предпоследнего элемента из деки
        self.assertListEqual(self.comparable(self.dq), [3])
        self.assertEqual(self.dq.head.value, 3)
        self.assertEqual(self.dq.tail.value, 3)

        self.assertEqual(self.dq.removeFront(), 3) # Удаление последнего элемента из деки
        self.assertListEqual(self.comparable(self.dq), [])
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)

        self.assertIsNone(self.dq.removeFront()) # Удаление из пустой деки
        self.assertListEqual(self.comparable(self.dq), [])
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)

    def test_removeTail(self) -> None:
        self.dq.addTail(1)
        self.dq.addTail(2)
        self.dq.addTail(3)

        self.assertEqual(self.dq.removeTail(), 3) # Удаление элемента из деки
        self.assertListEqual(self.comparable(self.dq), [1, 2])
        self.assertEqual(self.dq.head.value, 1)
        self.assertEqual(self.dq.tail.value, 2)

        self.assertEqual(self.dq.removeTail(), 2) # Удаление предпоследнего элемента из деки
        self.assertListEqual(self.comparable(self.dq), [1])
        self.assertEqual(self.dq.head.value, 1)
        self.assertEqual(self.dq.tail.value, 1)

        self.assertEqual(self.dq.removeTail(), 1) # Удаление последнего элемента из деки
        self.assertListEqual(self.comparable(self.dq), [])
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)

        self.assertIsNone(self.dq.removeTail()) # Удаление из пустой деки
        self.assertListEqual(self.comparable(self.dq), [])
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)

    def test_size(self) -> None:
        self.assertEqual(self.dq.size(), 0) # Проверка длинны пустой деки

        self.dq.addFront(1) # Изменение длинны при добавлении в начало
        self.assertEqual(self.dq.size(), 1)

        self.dq.removeFront() # Изменение длинны при удалении с начала
        self.assertEqual(self.dq.size(), 0)

        self.dq.addTail(1) # Изменение длинны при добавлении в конец
        self.assertEqual(self.dq.size(), 1)

        self.dq.removeTail() # Изменение длинны при удалении с конца
        self.assertEqual(self.dq.size(), 0)

        self.dq.removeFront() # Удаление с начала пустой деки
        self.assertEqual(self.dq.size(), 0)
        
        self.dq.removeTail() # Удаление с конца пустой деки
        self.assertEqual(self.dq.size(), 0)
        
    def test_mixed_deque(self):
        self.assertIsNone(self.dq.removeFront())
        self.assertIsNone(self.dq.removeTail())
        self.assertIsNone(self.dq.head)
        self.assertIsNone(self.dq.tail)

        self.dq.addFront(1)
        self.assertListEqual(self.comparable(self.dq), [1])
        self.assertListEqual(self.inverse_comparable(self.dq), [1])
        self.assertEqual(self.dq.head.value, 1)
        self.assertEqual(self.dq.tail.value, 1)

        self.dq.addTail(3)
        self.assertListEqual(self.comparable(self.dq), [1, 3])
        self.assertListEqual(self.inverse_comparable(self.dq), [3, 1])
        self.assertEqual(self.dq.head.value, 1)
        self.assertEqual(self.dq.tail.value, 3)

        self.dq.addFront(4)
        self.assertListEqual(self.comparable(self.dq), [4, 1, 3])
        self.assertListEqual(self.inverse_comparable(self.dq), [3, 1, 4])
        self.assertEqual(self.dq.head.value, 4)
        self.assertEqual(self.dq.tail.value, 3)
        
    def comparable(self, obj) -> list:
        node = obj.head
        res = []
        while node is not None:
            res.append(node.value)
            node = node.next
        return res
    
    def inverse_comparable(self, obj) -> list:
        node = obj.tail
        res = []
        while node is not None:
            res.append(node.value)
            node = node.prev
        return res
