
def outer():
  enclosing_variable = "Enclosing variable"
  
  def inner():
    nonlocal enclosing_variable # is similar to global but not as global
    # this is for looking outer the function regardless the scope
    enclosing_variable = "Modified enclosing"
  
  inner()
  print(enclosing_variable)

outer()