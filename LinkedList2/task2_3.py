import unittest
from algo import LinkedList2, Node

class TestLinkedListFunc(unittest.TestCase):
    def setUp(self):
        self.l1 = LinkedList2()
        self.l1.add_in_tail(Node(1))
        self.l1.add_in_tail(Node(2))
        self.l1.add_in_tail(Node(3))
        self.l1.add_in_tail(Node(4))
        self.l1.add_in_tail(Node(5))
        
        self.l2 = LinkedList2()
        
    def test_find(self):        
        self.assertIsInstance(self.l1.find(1), Node) # Проверка на возвращаемый тип данных
        
        self.assertEqual(self.l1.find(2).value, 2) # Поиск значения из списка
        
        self.assertIsNone(self.l1.find(21)) # Поиск значения не из списка
        
    def test_find_all(self):
        self.l1.add_in_tail(Node(2)) # Поиск нескольких Node с одинаковым значением
        self.assertListEqual(self.comparable(self.l1.find_all(2)), [2, 2])
        
        self.assertListEqual(self.comparable(self.l2.find_all(1)), []) # Поиск по пустому LinkedList
        
    def test_delete(self):
        self.l1.delete(1) # Удаление элемента из начала
        self.assertListEqual(self.comparable(self.l1), [2, 3, 4, 5])
        self.assertListEqual(self.comparable(self.l1, True), [5, 4, 3, 2])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 5)
        
        self.l1.delete(3) # Удаление элемента из середины
        self.assertListEqual(self.comparable(self.l1), [2, 4, 5])
        self.assertListEqual(self.comparable(self.l1, True), [5, 4, 2])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 5)

        self.l1.delete(5) # Удаление элемента из конца
        self.assertListEqual(self.comparable(self.l1), [2, 4])
        self.assertListEqual(self.comparable(self.l1, True), [4, 2])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 4)
    
        self.l1.delete(4) # Удаление предпоследнего элемента
        self.assertListEqual(self.comparable(self.l1), [2])
        self.assertListEqual(self.comparable(self.l1, True), [2])
        self.assertEqual(self.l1.head.value, 2)
        self.assertEqual(self.l1.tail.value, 2)
        
        self.l1.delete(2) # Удаление последнего элемента
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertListEqual(self.comparable(self.l1, True), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
        
        self.l1.delete(41) # Удаление несуществующего элемента из пустого списка
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertListEqual(self.comparable(self.l1, True), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)
    
    def test_clean(self):
        self.l1.clean() # Очистка наполненного списка
        self.assertListEqual(self.comparable(self.l1), [])
        self.assertListEqual(self.comparable(self.l1, True), [])
        self.assertIsNone(self.l1.head)
        self.assertIsNone(self.l1.tail)

        self.l2.clean() # Очистка пустого списка
        self.assertIsNone(self.l2.head)
        self.assertIsNone(self.l2.tail)

    def test_insert(self):
        self.l1.insert(self.l1.find(1), Node(10)) # Вставка в начало
        self.assertListEqual(self.comparable(self.l1), [1, 10, 2, 3, 4, 5])
        self.assertListEqual(self.comparable(self.l1, True), [5, 4, 3, 2, 10, 1])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 5)

        self.l1.insert(self.l1.find(3), Node(11)) # Вставка в середину
        self.assertListEqual(self.comparable(self.l1), [1, 10, 2, 3, 11, 4, 5])
        self.assertListEqual(self.comparable(self.l1, True), [5, 4, 11, 3, 2, 10, 1])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 5)

        self.l1.insert(self.l1.find(5), Node(12)) # Вставка в конец
        self.assertListEqual(self.comparable(self.l1), [1, 10, 2, 3, 11, 4, 5, 12])
        self.assertListEqual(self.comparable(self.l1, True), [12, 5, 4, 11, 3, 2, 10, 1])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 12)

        self.l1.insert(self.l1.find(100), Node(100)) # Вставка если afterNode не найден
        self.assertListEqual(self.comparable(self.l1), [1, 10, 2, 3, 11, 4, 5, 12, 100])
        self.assertListEqual(self.comparable(self.l1, True), [100, 12, 5, 4, 11, 3, 2, 10, 1])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 100)

        self.l1.insert(None, Node(101)) # Вставка если afterNode = None
        self.assertListEqual(self.comparable(self.l1), [1, 10, 2, 3, 11, 4, 5, 12, 100, 101])
        self.assertListEqual(self.comparable(self.l1, True), [101, 100, 12, 5, 4, 11, 3, 2, 10, 1])
        self.assertEqual(self.l1.head.value, 1)
        self.assertEqual(self.l1.tail.value, 101)

        self.l2.insert(None, Node(1)) # Вставка в пустой LinkedList
        self.assertListEqual(self.comparable(self.l2), [1])
        self.assertListEqual(self.comparable(self.l2, True), [1])
        self.assertEqual(self.l2.head.value, 1)
        self.assertEqual(self.l2.tail.value, 1)
        
        self.l2.insert(self.l1.find(3), Node(2)) # Вставка элемента из другого LinkedList
        self.assertListEqual(self.comparable(self.l2), [1])
        self.assertListEqual(self.comparable(self.l2, True), [1])
        self.assertEqual(self.l2.head.value, 1)
        self.assertEqual(self.l2.tail.value, 1)

    def test_add_in_head(self):
        self.l1.add_in_head(Node(10)) # Добавление Node в непустой LinkedList
        self.assertListEqual(self.comparable(self.l1), [10, 1, 2, 3, 4, 5])
        self.assertListEqual(self.comparable(self.l1, True), [5, 4, 3, 2, 1, 10])
        self.assertEqual(self.l1.head.value, 10)
        self.assertEqual(self.l1.tail.value, 5)

        self.l2.add_in_head(Node(1)) # Добавление Node в пустой LinkedList
        self.assertListEqual(self.comparable(self.l2), [1])
        self.assertListEqual(self.comparable(self.l2, True), [1])
        self.assertEqual(self.l2.head.value, 1)
        self.assertEqual(self.l2.tail.value, 1)

    def test_reverse(self):
        self.l2.add_in_head(Node(5)) # Переворот LinkedList'а из одного элемента
        self.l2.reverse()
        self.assertListEqual(self.comparable(self.l2), [5])
        self.assertEqual(self.l2.head.value, 5)
        self.assertEqual(self.l2.tail.value, 5)
        
        self.l2.add_in_head(Node(2)) # Переворот LinkedList'а из двух элементов
        self.l2.reverse()
        self.assertListEqual(self.comparable(self.l2), [5, 2])
        self.assertEqual(self.l2.head.value, 5)
        self.assertEqual(self.l2.tail.value, 2)
        
        self.l1.reverse() # Переворот наполненного LinkedList
        self.assertListEqual(self.comparable(self.l1), [5, 4, 3, 2, 1])
        self.assertEqual(self.l1.head.value, 5)
        self.assertEqual(self.l1.tail.value, 1)

    def comparable(self, obj, reverse=False) -> list:
      res = list()
      if isinstance(obj, LinkedList2):
          node = obj.head if reverse == False else obj.tail
          while node is not None:
              res.append(node.value)
              node = node.next if reverse == False else node.prev
      else:
          for node in obj:
              res.append(node.value)
      return res
        
        
if __name__ == "__main__":
    unittest.main()
