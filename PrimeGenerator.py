from abc import ABCMeta, abstractmethod

class  PrimeNumberGeneratorInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def generate(self): raise NotImplementedError

    @abstractmethod
    def is_prime(self): raise NotImplementedError

class PrimeNumberGenerator(PrimeNumberGeneratorInterface):
    def generate(self, start, end):
        numbers = []
        small = min(start,end)
        large = max(start,end)
        for i in range(small,large+1):
            if self.is_Prime(self,i):
                numbers.append(i)
        return numbers

    def is_Prime(self, value):
        n=abs(value)
        if n==2 or n==3: return True
        if n%2==0 or n<2: return False
        for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
            if n%i==0:
                return False    
        return True

    def show(self):
        print("Hello, World")


