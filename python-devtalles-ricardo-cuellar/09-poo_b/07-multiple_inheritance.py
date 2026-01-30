class Flyer:
  def fly(self):
    print("I can fly!")
  
  def do_something(self):
    print("Flying")

class Swimmer:
  def swim(self):
    print("I can swim!")
  
  def do_something(self):
    print("Swimming")


# multiple class inheritance
class Duck(Flyer, Swimmer):
  def quack(self):
    print("Quack")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()

# this is going to trigger the first method due MRO
# MRO: Method Resolution Order
duck.do_something() # flying


# MRO
print(Duck.__mro__) # (<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)