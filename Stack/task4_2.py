# Задание 4.5.
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
    
# Задание 4.6.
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

# Рефлексия по заданию 4.6.
# Альтернативным решением является использования словаря, который поможет выявлять пару для открывающих скобок.
# В текущем решении используется ASCII-таблица для определения типа скобок, что никак не влияет на асимптотическую и пространственную сложности, если сравнивать с альтернативой.

# Задание 4.7.
# Асимптотическая сложность O(n).
# Пространственная сложность O(2n) - т.к. создаем два стека с одинаковым кол-вом элементов.
class StackWithMin:
    def __init__(self):
        self.main = Stack()
        self.min = Stack()

    def size(self):
        return self.main.size()

    def pop(self):
        if self.main.size() == 0:
            return None
        self.min.pop()
        return self.main.pop()

    def push(self, value):
        self.main.push(value)
        if self.min.size() == 0:
            self.min.push(value)
        else:
            self.min.push(min(value, self.min.peek()))

    def peek(self):
        return self.main.peek()

    def get_min(self):
        if self.min.size() == 0:
            return None
        return self.min.peek()
    
# Рефлексия по заданию 4.7.
# Альтернативным решением может быть запись минимального значения не в отдельный элемент, а в переменную. 
# Но в таком случае код не будет корректно работать при удалении из стека, т.к. не сможет воспроизвести предыдущие минимальные значения.

# Задание 4.8.
# Асимптотическая сложность O(1).
# Пространственная сложность O(1).
class Node_1:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None

class StackAvg:
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
        node = Node_1(value)
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
# Текущая реализация работает за O(1) из-за создания новой переменной, в которой накапливается сумма всех элементов стека.
    
# Задание 4.9.
# Асимптотическая сложность O(n) - проходим по всему выражению.
# Пространственная сложность O(n) - кол-во добавляемых элементов в стек зависит от кол-ва элементов в выражении.
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
        return operand2 * operand1
    elif operator == '/':
        return operand2 / operand1
    elif operator == '+':
        return operand2 + operand1
    elif operator == '-':
        return operand2 - operand1
    else:
       return -1
        
# Рефлексия по заданию 4.9.
# Альтернативным решением может являться использование Python списков (list) вместо стека.
# При использовании динамического массива вставка и удаление могут вызывать реаллокацию массива, из-за чего временная сложность может доходить до O(n).
# Текущий вариант, поскольку опирается на реализацию односвязных списков, исключает реаллокации.
