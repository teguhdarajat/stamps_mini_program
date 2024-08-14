import math

class MiniProgram:
    def __init__(self, number) -> None:
        self.number = number
    
    def is_prime(self, n) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def get_numbers(self):
        numbers = []
        for i in reversed(range(1, self.number+1)):
            if self.is_prime(i):
                continue
            elif (i % 3 == 0) and (i % 5 == 0):
                numbers.append("FooBar")
            elif (i % 3 == 0):
                numbers.append("Foo")
            elif(i % 5 == 0):
                numbers.append("Bar")
            else:
                numbers.append(i)
        return numbers