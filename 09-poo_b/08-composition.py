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
# class Duck(Flyer, Swimmer):

# COMPOSITION
# less coupled than inheritance
class Duck():
  
  def __init__(self):
    # composition
    self.flyer = Flyer()
    self.swimmer = Swimmer()

  def quack(self):
    print("Quack")
  
  def start_fly(self):
    self.flyer.fly()
    
  def start_swim(self):
    self.swimmer.swim()
  
  def do_something(self):
    self.swimmer.do_something()
    self.flyer.do_something()

duck = Duck()
duck.start_fly()
duck.start_swim()
duck.do_something()
duck.quack()
