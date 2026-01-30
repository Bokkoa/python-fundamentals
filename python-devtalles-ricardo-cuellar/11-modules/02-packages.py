# from my_package import math_utils, messages

# print(math_utils.addition(3, 2))
# print(messages.greet("Felipe"))
# print(messages.bye("Felipe"))

# using barrell technique
from my_package import addition, greet, bye

print(addition(3, 2))
print(greet("Felipe"))
print(bye("Felipe"))