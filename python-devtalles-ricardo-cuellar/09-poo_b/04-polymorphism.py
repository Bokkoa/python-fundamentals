class Animal:
  def make_sound(self):
    print("Default sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow meow!")

def make_noise(animal):
  if isinstance(animal, Animal):
    animal.make_sound()
  else:
    print("This is not an animal")

make_noise(Dog())
make_noise(Cat())
make_noise("Hello world")