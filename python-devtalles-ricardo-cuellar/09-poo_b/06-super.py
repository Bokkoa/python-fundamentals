
class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def sound(self):
    print(f"{self.name} does some sound")

  def info(self):
    print(f"I'm {self.name} and I'm {self.age} years old")

class Dog(Animal):
  
  def __init__(self, name, age, breed):
    # calling parent constructor
    super().__init__(name, age)
    self.breed = breed
  
  def sound(self):
    # accessing parent class method
    super().sound()
    print(f"{self.name} says Woof")
    
  def info(self):
    super().info()
    print(f"I'm {self.breed} breed")

class Cat(Animal):
  def sound(self):
    print(f"{self.name} says Meow")

ginger = Dog("Ginger", 5, "Mix")
ginger.sound() # Tom does some sound
            # Tom says Woof
            
ginger.info()
