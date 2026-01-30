# Scope
# is the context of our instructions in the program

# Is global because is in the root scope
global_variable = "I'm global"


def outer_function():
  enclosing_variable = "I'm enclosing var"
  
  def inner_function():
    local_variable = "I'm local"
    
    print(global_variable)
    print(enclosing_variable)
    print(local_variable)
  
  inner_function()
  # print(local_variable) # this variable is not defined in this scope
  
outer_function()