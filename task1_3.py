import unittest
from algo import LinkedList, Node

class TestLinkedListFunc(unittest.TestCase):
    def setUp(self):
        self.l1 = LinkedList()
        self.l1.add_in_tail(Node(1))
        self.l1.add_in_tail(Node(2))
        self.l1.add_in_tail(Node(3))
        self.l1.add_in_tail(Node(4))
        self.l1.add_in_tail(Node(5))
        
        self.l2 = LinkedList()
        
        
    def test_delete(self):
        self.l1.delete(1) # Удаление первого элемента
        self.assertListEqual(self.comparable(self.l1), [2, 3, 4, 5])
        self.assertEqual(self.l1.head.value, 2)
        
        self.l1.delete(5) # Удаление последнего элемента
        self.assertListEqual(self.comparable(self.l1), [2, 3, 4])
        self.assertEqual(self.l1.tail.value, 4)
        
        self.l1.delete(3) # Удаление из середины
        self.assertListEqual(self.comparable(self.l1), [2, 4])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 4)
        
        self.l1.delete(1) # Удаление несуществующего элемента
        self.assertListEqual(self.comparable(self.l1), [2, 4])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 4)
        
        self.l1.delete(4) # Удаление предпоследнего элемента из списка
        self.assertListEqual(self.comparable(self.l1), [2])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 2)
        
        self.l1.delete(2) # Удаление последенего элемента списка
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
        
        self.l1.delete(3) # Удаление несуществующего элемента из пустого списка
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
        
    def test_delete_all(self):
        self.l1.add_in_tail(Node(3))
        self.l1.add_in_tail(Node(3))
        self.l1.delete(3, True) # Удаление элементов из середины и конца
        self.assertListEqual(self.comparable(self.l1), [1, 2, 4, 5])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.add_in_tail(Node(1))
        self.l1.add_in_tail(Node(1))
        self.l1.delete(1, True) # Удаление элементов из начала и конца
        self.assertListEqual(self.comparable(self.l1), [2, 4, 5])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.delete(1, True) # Удаление несуществующего элемента
        self.assertListEqual(self.comparable(self.l1), [2, 4, 5])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.delete(4, True) # Удаление из середины
        self.assertListEqual(self.comparable(self.l1), [2, 5])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.delete(2, True) # Удаление первого элемента
        self.assertListEqual(self.comparable(self.l1), [5])
        self.assertEqual(self.l1.head.value, 5)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.delete(5, True) # Удаление последнего элемента
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
    
    def test_clean(self):
        self.l1.clean() # Отчистка наполненного LinkedList
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
        
        self.l2.clean() # Отчистка пустого LinkedList
        self.assertListEqual(self.comparable(self.l2), [])
        self.assertIsNone(self.l2.head)
        self.assertIsNone(self.l2.tail)
    
    def test_find_all(self):
        self.assertIsInstance(self.l1.find_all(1), list) # Проверка на возвращение list
        self.assertIsInstance(self.l1.find_all(1)[0], Node) # Проверка на элемент Node в list
        
        self.l1.add_in_tail(Node(1)) # Поиск элементов из начала и конца
        self.assertListEqual(self.comparable(self.l1.find_all(1)), [1, 1])
        
        self.assertListEqual(self.comparable(self.l1.find_all(10)), []) # Поиск несуществующего элемента
        
        self.assertListEqual(self.comparable(self.l2.find_all(10)), []) # Поиск по пустому списку
    
    def test_len(self):
        self.assertEqual(self.l1.len(), 5)
        self.l1.add_in_tail(Node(5))
        self.l1.add_in_tail(Node(5))
        self.l1.add_in_tail(Node(5)) # добавление 3х node
        self.assertEqual(self.l1.len(), 8)
        
        self.l1.delete(5, True) # Удаление всех node.value = 5
        self.assertEqual(self.l1.len(), 4)
        
        self.l1.clean() # Размер пустого LinkedList
        self.assertEqual(self.l1.len(), 0)

    def test_insert(self):
        self.l1.insert(self.l1.find(1), Node(3)) # Вставка после первого элемента
        self.assertListEqual(self.comparable(self.l1), [1, 3, 2, 3, 4, 5])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 5)
        

        self.l1.insert(self.l1.find(5), Node(7),) # Вставка после последнего элемента
        self.assertListEqual(self.comparable(self.l1), [1, 3, 2, 3, 4, 5, 7])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 7)

        self.l1.add_in_tail(Node(2))
        self.l1.add_in_tail(Node(2))
        self.l1.insert(self.l1.find(2), Node(100)) # Вставка в середину
        self.assertListEqual(self.comparable(self.l1), [1, 3, 2, 100, 3, 4, 5, 7, 2, 2])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 2)
        
        self.l1.insert(self.l1.find(422), Node(400)) # Вставка после несуществующего элемента
        self.assertListEqual(self.comparable(self.l1), [400, 1, 3, 2, 100, 3, 4, 5, 7, 2, 2])
        self.assertEqual(self.l1.head.value, 400)
        self.assertEqual(self.l1.tail.value, 2)
        
        self.l2.insert(None, Node(200)) # Вставка в пустой LinkedList
        self.assertListEqual(self.comparable(self.l2), [200])
        self.assertEqual(self.l2.head.value, 200)
        self.assertEqual(self.l2.tail.value, 200)
        
        
    def comparable(self, obj) -> list:
        res = list()
        if isinstance(obj, LinkedList):
            node = obj.head
            while node is not None:
                res.append(node.value)
                node = node.next
        else:
            for node in obj:
                res.append(node.value)
        return res
        
        
if __name__ == "__main__":
    unittest.main()
