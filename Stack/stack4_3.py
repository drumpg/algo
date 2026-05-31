import unittest
from algo import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack()

    # Тесты для задания 4.1
    # def test_push(self):
    #     self.stack1.push(1) # Добавление элементов в стек
    #     self.stack1.push(2)
    #     self.stack1.push(5)
    #     self.assertListEqual(self.comparable(self.stack1), [1, 2, 5])
        
    # def test_pop(self):
    #     self.stack1.push(1)
    #     self.stack1.push(2)
    #     self.stack1.push(3)

    #     self.assertEqual(self.stack1.pop(), 3) # Удаление элемента из стека
    #     self.assertListEqual(self.comparable(self.stack1), [1, 2])

    #     self.assertEqual(self.stack1.pop(), 2) # Удаление предпоследнего элемента из стека
    #     self.assertListEqual(self.comparable(self.stack1), [1])

    #     self.assertEqual(self.stack1.pop(), 1) # Удаление последнего элемента из стека
    #     self.assertListEqual(self.comparable(self.stack1), [])
        
    #     self.assertEqual(self.stack1.pop(), None) # Удаление из пустого стека
        
    # def test_peek(self):
    #     self.assertIsNone(self.stack1.stack.head) # Вывод первого (пустого) элемента из стека
    #     self.assertEqual(self.stack1.len, 0)
    #     self.assertListEqual(self.comparable(self.stack1), [])

    #     self.stack1.push(1) # Вывод единственного элемента из стека
    #     self.assertEqual(self.stack1.peek(), 1)

    #     self.stack1.push(2) # Вывод первого элемента из стека, после добавление нового элемента
    #     self.assertEqual(self.stack1.peek(), 2)
        
    # def test_size(self):
    #     self.assertEqual(self.stack1.size(), 0) # Размер пустого стека

    #     self.stack1.push(5)
    #     self.assertEqual(self.stack1.size(), 1) # Размер стека из одного элемента

    #     self.stack1.push(4)
    #     self.assertEqual(self.stack1.size(), 2) # Размер стека из нескольких элементов

    #     self.stack1.pop()
    #     self.assertEqual(self.stack1.size(), 1) # Размер стека при удалении одного из элементов

    #     self.stack1.pop()
    #     self.assertEqual(self.stack1.size(), 0) # Размер стека при удалении всех элементов
        
    # def comparable(self, obj) -> list:
    #     res = []
    #     node = obj.stack.head
    #     while node is not None:
    #         res.append(node.val)
    #         node = node.next

    #     return res
    
    # Тесты для задания 4.2
    def test_push(self):
        self.stack1.push(1) # Добавление элементов в стек
        self.stack1.push(2)
        self.stack1.push(5)
        self.assertListEqual(self.comparable(self.stack1), [5, 2, 1])

    def test_pop(self):
        self.stack1.push(1)
        self.stack1.push(2)
        self.stack1.push(3)

        self.assertEqual(self.stack1.pop(), 3) # Удаление элемента из стека
        self.assertListEqual(self.comparable(self.stack1), [2, 1])

        self.assertEqual(self.stack1.pop(), 2) # Удаление предпоследнего элемента из стека
        self.assertListEqual(self.comparable(self.stack1), [1])

        self.assertEqual(self.stack1.pop(), 1) # Удаление последнего элемента из стека
        self.assertListEqual(self.comparable(self.stack1), [])
    
        self.assertEqual(self.stack1.pop(), None) # Удаление из пустого стека


    def test_peek(self):
        self.assertIsNone(self.stack1.stack) # Вывод первого (пустого) элемента из стека
        self.assertEqual(self.stack1.len, 0)
        self.assertListEqual(self.comparable(self.stack1), [])

        self.stack1.push(1) # Вывод единственного элемента из стека
        self.assertEqual(self.stack1.peek(), 1)

        self.stack1.push(2) # Вывод первого элемента из стека, после добавление нового элемента
        self.assertEqual(self.stack1.peek(), 2)

    def test_size(self):
        self.assertEqual(self.stack1.size(), 0) # Размер пустого стека

        self.stack1.push(5)
        self.assertEqual(self.stack1.size(), 1) # Размер стека из одного элемента

        self.stack1.push(4)
        self.assertEqual(self.stack1.size(), 2) # Размер стека из нескольких элементов

        self.stack1.pop()
        self.assertEqual(self.stack1.size(), 1) # Размер стека при удалении одного из элементов

        self.stack1.pop()
        self.assertEqual(self.stack1.size(), 0) # Размер стека при удалении всех элементов

    def comparable(self, obj) -> list:
        res = []
        node = obj.stack
        while node is not None:
            res.append(node.val)
            node = node.next

        return res
