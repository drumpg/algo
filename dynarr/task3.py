import ctypes

class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
    
    # Асимтотическая оценка O(n) - т.к. в худшем случае необходимо пройти по всему массиву, чтобы вставить новый "itm" на позицию "i".
    # Пространственная оценка O(1) - не аллоцируем новый массив.
    def insert(self, i, itm) -> None:
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")

        self.append(itm)
        
        for j in range(self.count-1, -1, -1):
            if j == i:
                break   
            self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
    
    # Асимптотическая оценка O(n) - т.к. в худшем случае проходим по всему массиву (тащим элемент с начала до конца).
    # Пространственная оценка O(1) - не аллоцируем новый массив.
    def delete(self, i) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
                
        for j in range(self.count-1):
            if j < i:
                continue
            
            self.array[j] = self.array[j+1]
            
        self.array[self.count-1] = None
        self.count -= 1
        self.realloc()
            
    def realloc(self) -> None:
        ratio = int((self.count / self.capacity) * 100)
        new_cap = int(self.capacity / 1.5)
        if ratio < 50 and self.capacity > 16:
            self.resize(max(new_cap, 16))
