

# in
# not in

print(9 in range(1, 10)) # True
print(10 in range(1, 10)) # False (from 0 to 9)

fruits = ["Apple", "Banana", "Strawberry"]

print("Banana" in fruits) # True
print("Banana" not in fruits) # False
print("Mango" not in fruits) # True

sentence = "I'm Python programmer, but also I know JS, Typescript and Go"

print("Python" in sentence) # True
print("Scala" in sentence) # False