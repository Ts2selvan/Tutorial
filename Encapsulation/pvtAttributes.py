# Private Attributes with Getter and Setter Methods

class Person:
    def __init__(self, name,age):
        self.__name=name
        self.__age=age

    def getName(self):
        return self.__name

    # def setAge(self,age):
    #     if age > 0:
    #       return self.__age= age


person=Person("John",18)
print(person.getName())
print(person.__name)