# Docstring
# Is a comment that can works as documentation
def hello(greet = "Hello", name = "Guest"):
  """
  Info: this is a function for print a customized greet
  """
  print(f"{greet}, {name}")
  
hello("Hola", "Mundo")


# Adding some types to our arguments as a:float
def multiply(a: float, b: float) -> float:  # Declare the kind of returning
  """
  Info: It multiplies two numbers and return the product
  """
  return a * b

print(multiply(2, 4))