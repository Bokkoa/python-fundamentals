# importing all the library
import math 
print(math.sqrt(16))


# importing specific methods
# it save memory
from datetime import datetime
print(datetime.now())


# Importing using alias
import random as rand
print(rand.randint(1, 10))

# getting multiple methods
from math import sin, cos, pi
print(sin(pi/2))
print(cos(0))

# importing everything but
# at single level (without pointing math first)
from math import *

