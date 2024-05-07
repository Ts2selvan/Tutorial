# Private Methods

class Calci:
    def __init__(self):
        pass
    def __add(self, a, b):
        return a + b
    def __sub(self, a, b):
        return a - b
    def calculation(self,a,b):
        add=self.__add(a,b)
        sub=self.__sub(a,b)
        return add, sub

calci=Calci()
result=calci.calculation(10,7)
print(f"{result[0]} , {result[1]} ")
