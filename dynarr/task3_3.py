import unittest
from task3 import DynArray

class TestDynArray(unittest.TestCase):
    def setUp(self):
        self.arr1 = DynArray()
        self.arr1.append(1)
        self.arr1.append(5)
        self.arr1.append(3)
        self.arr1.append(4)
        self.arr1.append(8)
        self.arr1.append(10)

    def test_insert(self):
        with self.assertRaises(IndexError): # Вставка за пределы массива (< 0)
            self.arr1.insert(-1, 1)

        with self.assertRaises(IndexError): # Вставка за пределы массива (> max)
            self.arr1.insert(self.arr1.count+1, 1)

        self.arr1.insert(4, 100) # Вставка в середину
        self.assertListEqual(self.comparable(self.arr1), [1, 5, 3, 4, 100, 8, 10])
        self.assertEqual(self.arr1.count, 7)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.insert(0, 101) # Вставка в начало
        self.assertListEqual(self.comparable(self.arr1), [101, 1, 5, 3, 4, 100, 8, 10])
        self.assertEqual(self.arr1.count, 8)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.insert(self.arr1.count, 11) # Вставка в конец
        self.assertListEqual(self.comparable(self.arr1), [101, 1, 5, 3, 4, 100, 8, 10, 11])
        self.assertEqual(self.arr1.count, 9)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.insert(1, 1000) # Увеличение емкости
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.arr1.insert(1, 1000)
        self.assertListEqual(self.comparable(self.arr1), [101, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 5, 3, 4, 100, 8, 10, 11])
        self.assertEqual(self.arr1.count, 17)
        self.assertEqual(self.arr1.capacity, 32)

    def test_delete(self):
        with self.assertRaises(IndexError): # Удаление за пределами массива (< 0)
            self.arr1.delete(-1)

        with self.assertRaises(IndexError): # Удаление за пределами массива (> max)
            self.arr1.delete(self.arr1.count)

        self.arr1.delete(0) # Удаление первого элемента
        self.assertListEqual(self.comparable(self.arr1), [5, 3, 4, 8, 10])
        self.assertEqual(self.arr1.count, 5)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.delete(self.arr1.count-1)
        self.assertListEqual(self.comparable(self.arr1), [5, 3, 4, 8])
        self.assertEqual(self.arr1.count, 4)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.append(1) # Увеличение емкости
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.arr1.append(1)
        self.assertListEqual(self.comparable(self.arr1), [5, 3, 4, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(self.arr1.count, 17)
        self.assertEqual(self.arr1.capacity, 32)

        self.arr1.delete(0) # Уменьшение емкости
        self.arr1.delete(0)
        self.assertListEqual(self.comparable(self.arr1), [4, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(self.arr1.count, 15)
        self.assertEqual(self.arr1.capacity, 21)

        self.arr1.delete(0) # Уменьшение емкости (не может быть меньше 16)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.assertListEqual(self.comparable(self.arr1), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(self.arr1.count, 10)
        self.assertEqual(self.arr1.capacity, 16)

        self.arr1.delete(0) # Удаление всех элементов из массива
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.assertEqual(self.arr1.capacity, 16)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.assertEqual(self.arr1.capacity, 16)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.arr1.delete(0)
        self.assertListEqual(self.comparable(self.arr1), [])
        self.assertEqual(self.arr1.count, 0)
        self.assertEqual(self.arr1.capacity, 16)

        with self.assertRaises(IndexError): # Удаление из пустого массива
            self.arr1.delete(0)

    def comparable(self, obj) -> list:
        res = []
        for i in obj:
            res.append(i)
        return res
