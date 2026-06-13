import unittest
from algo import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_enqueue(self):
        self.assertListEqual(self.comparable(self.q), []) # Проверка пустой очереди
        self.assertEqual(self.q.size(), 0)
        self.assertIsNone(self.q.head)
        self.assertIsNone(self.q.tail)
        
        self.q.enqueue(1) # Добавление одного элемента в очередь
        self.assertListEqual(self.comparable(self.q), [1])
        self.assertEqual(self.q.size(), 1)
        self.assertEqual(self.q.head.value, 1)
        self.assertEqual(self.q.tail.value, 1)
        
        self.q.enqueue(2) # Добавление нескольких элементов в очередь
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.assertListEqual(self.comparable(self.q), [1, 2, 3, 4])
        self.assertEqual(self.q.size(), 4)
        self.assertEqual(self.q.head.value, 1)
        self.assertEqual(self.q.tail.value, 4)
                
    def test_dequeue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

        self.q.dequeue() # Удаление одного значения из очереди 
        self.assertListEqual(self.comparable(self.q), [2, 3])
        self.assertEqual(self.q.size(), 2)
        self.assertEqual(self.q.head.value, 2)
        self.assertEqual(self.q.tail.value, 3)
        
        self.q.dequeue() # Удаление всех значений из очереди
        self.q.dequeue()
        self.assertListEqual(self.comparable(self.q), [])
        self.assertEqual(self.q.size(), 0)
        self.assertIsNone(self.q.head)
        self.assertIsNone(self.q.tail)

        self.q.dequeue() # Удаление из пустой очереди
        self.assertListEqual(self.comparable(self.q), [])
        self.assertEqual(self.q.size(), 0)
        self.assertIsNone(self.q.head)
        self.assertIsNone(self.q.tail)
        

    def comparable(self, obj) -> list:
        res = []
        node = obj.head
        while node is not None:
            res.append(node.value)
            node = node.next

        return res
