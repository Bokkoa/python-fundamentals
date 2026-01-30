# reusable code blocks

# CLEAN RULE
# EVERY FUNCTION SHOULD DO JUST ONE THING
def hello():
  print("Hello world from function")

  return "Hello from RETURN"

def bye():
  print("Bye world from funciton")
  
  return 2 + 2

hello()
bye()

print(hello()) # Hello from RETURN
print(bye()) # 4
