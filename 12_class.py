# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hello {self.name}, Good Morning ;)")
#
# person = Person('Dicki')
# person.talk()

class Mammal:
    def talk(self):
        print("Talk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    def meow(self):
        print("Meow")

dog = Dog()
dog.talk()

cat = Cat()
cat.talk()
cat.meow()