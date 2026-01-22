
class Animal:
  def __init__(self, name):
    self.name = name
  
  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def dog_sound(self):
    print(f"{self.name} says Woof")

class Cat(Animal):
  def cat_sound(self):
    print(f"{self.name} says Meow")
    
    
firulais = Dog("Firulais")
firulais.sleep()
firulais.dog_sound()

malva = Cat("Malva")
malva.sleep()
malva.cat_sound()