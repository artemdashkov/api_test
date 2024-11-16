class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Определяем производный класс
class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"


class Cow(Animal):
    def __init__(self, name, weight):
        # Animal.__init__(self, name)
        super().__init__(name)
        self.weight = weight
    def speak(self):
        return "Moo"

# Создаем экземпляры производных классов
dog = Dog("Rex")
cat = Cat("Mittens")
cow = Cow("Marta", 300)

# Вызываем метод speak
print(dog.name + " says: " + dog.speak())  # Rex says: Bark
print(cat.name + " says: " + cat.speak())  # Mittens says: Meow
print(cow.name + " says: " + cow.speak(), "and weight is: " + str(cow.weight))  # Mittens says: Meow