# reusable code blocks

# CLEAN RULE
# EVERY FUNCTION SHOULD DO JUST ONE THING
def hello():
  print("Hello world from function")


def bye():
  print("Bye world from funciton")

hello()
bye()

print(hello()) # None (because my function is void and is not returning anything)