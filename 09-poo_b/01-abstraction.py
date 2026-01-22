class CoffeeMaker:
  
  def make_coffee(self):
    self.__boil_water()
    self.__mix()
    print("PIP PIP")
    print("Coffee is ready ☕")
  
  def __boil_water(self):
    print("Boiling water...")
  
  def __mix(self):
    print("Mixing coffee and water...")
  
  
coffee_maker = CoffeeMaker()
coffee_maker.make_coffee()