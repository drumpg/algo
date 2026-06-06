# Задание 4.5
# Асимптотическая оценка O(n) - проходим по каждому элементу переданной строки.
# Пространственная оценка O(m) - создаем стек размера m, где m - кол-во открывающих скобок в строке.
def is_balanced(string) -> bool:
    stack = Stack()
    for char in string:
        if char == "(":
            stack.push(char)

        if char == ")" and stack.size() == 0:
            return False

        if char == ")":
            stack.pop()

    return stack.size() == 0

# Рефлексия по заданию 4.5.
# Альтернативным решением является подсчет кол-ва открывающих и закрывающих скобок с помощью словаря.
# Создаем словарь и запускаем цикл в котором заносим значения "(" и ")" в словарь (в качестве ключа), каждый раз прибавляя +1 при повторной встрече.
# После этого проверяем равенство двух значений по ключам "(" и ")" и возвращаем результат.
# Асимптотическая оценка O(n) - остается прежней, т.к. мы должны пройти по всей строке в любом случае.
# Пространственная оценка O(1) - всегда имеем словарь из двух значений.
    
# Задание 4.6
# Асимптотическая сложность O(n) - т.к. должны пройти по всему выражению в любом случае.
# Пространственная сложность O(m) - создаем стек размера m, где m - кол-во открывающих скобок в строке.
def is_balanced(string) -> bool:
    stack = Stack()
    for char in string:
        if char in ('(', '{', '['):
            stack.push(char)

        if char in (')', '}', ']') and stack.size() == 0:
            return False

        if char in (')', '}', ']'):
            if (ord(char) // 10 == ord(stack.peek()) // 10):
                stack.pop()
            else:
                return False

# Рефлексия по заданию 4.7.
# Альтернативным решением является использования словаря, который поможет выявлять пару для открывающих скобок.
# В текущем решении используется ASCII-таблица для определения типа скобок, что никак не влияет на асимптотическую и пространственную сложности, если сравнивать с альтернативой.
    
# Задание 4.8
# Асимптотическая сложность O(1).
# Пространственная сложность O(1).
class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.stack = None
        self.len = 0
        self.sum = 0

    def size(self) -> int:
        return self.len

    def pop(self) -> int:
        if self.size() == 0:
            return None
        
        tmp = self.stack
        self.stack = self.stack.next
        self.len -= 1
        if isinstance(tmp.val, int):
            self.sum -= tmp.val
        return tmp.val

    def push(self, value) -> None:
        node = Node(value)
        node.next = self.stack
        self.stack = node
        self.len += 1
        if isinstance(value, int):
            self.sum += value

    def peek(self) -> any:
        return self.stack.val if self.size() > 0 else None

    def average(self) -> float:
        if self.len > 0:
            return self.sum / self.len
        return 0

# Рефлексия по заданию 4.8.
# Альтернативным решением является прохождение в цикле по всему стеку и вычисления среднего значения.
# Альтернативное решение работает за O(n) по времени, т.к. необходимо пройти по всем элементам стека.
# Текущая реализация работает за O(1) из-за создания новой переменной, в которой накапливается сумма всех элементов стека
    
# Задание 4.9
def polish(expression) -> int:
    stack = Stack()
    for elem in expression.split():
        if not elem.isdigit() and elem not in ('*', '/', '+', '-'):
            return -1
        
        if elem.isdigit():
            stack.push(int(elem))
            continue

        calculated = calc(stack.pop(), stack.pop(), elem)
        stack.push(calculated)
        
    return stack.peek()

def calc(operand1, operand2, operator) -> float:
    if operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    else:
       return -1
