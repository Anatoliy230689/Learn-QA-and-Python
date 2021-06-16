# ================= Инкапсуляция =================
class SomeClass:
    def _private(self):
        print("Это внутренний метод объекта")

a = SomeClass()
print(a._private())

# ======================================================================

class SomeClass():
    def __init__(self):
        self.__param = 42 # защищенный атрибут

obj = SomeClass()
# obj.__param # AttributeError: 'SomeClass' object has no attribute '__param'
print(obj._SomeClass__param )# 42

# ======================================================================

class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self): # получение значения атрибута
        return self._value

    def setvalue(self, value): # установка значения атрибута
        self._value = value

    def delvalue(self): # удаление атрибута
        del self._value

    value = property(getvalue, setvalue, delvalue, "Свойство value")

obj = SomeClass(42)
print(obj.value)
obj.value = 43
print(obj.value)

# ================= Наследование =================

class Mammal():
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print(dog.className) # Mammal
# ======================================================================
class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse, Donkey):
    pass
mule = Mule()
mule.isHorse # True
print(mule.isDonkey) # True
# ======================================================================

# ================= Полиморфизм =================

class Mammal:
    def move(self):
        print('Двигается')

class Hare(Mammal):
    def move(self):
        print('Прыгает')

animal = Mammal()
animal.move() # Двигается
hare = Hare()
print(hare.move()) # Прыгает