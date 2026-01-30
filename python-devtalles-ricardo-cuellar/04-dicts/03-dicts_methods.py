
# Methods

user = {
  "name": "Felipe",
  "age": 29,
  "greet": "Hola Mundo",
  "numbers": [1, 2, 3]
}


# get()
# obtaining a value by key
print(user.get('name'))


# in
# in only works using keys by default
print('name' in user)


# in used in keys explicitly
print('name' in user.keys())


# in used in values
print('Felipe' in user.values())


# items()
# return the dict's values
print(user.items())