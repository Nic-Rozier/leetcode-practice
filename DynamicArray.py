class DynamicArray:

    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.lst = [None] * capacity
            self.size = 0

    def get(self, i: int) -> int:
        return self.lst[i]

    def set(self, i: int, n: int) -> None:
        self.lst[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.lst[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.lst[self.size - 1]
        self.lst[self.size - 1] = None
        self.size -= 1
        return val

    def resize(self) -> None:
        new_lst = [None] * (self.capacity * 2)
        for i in range(len(self.lst)):
            new_lst[i] = self.lst[i]
        self.lst = new_lst
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity