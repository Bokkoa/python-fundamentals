# keys cannot be mutable
# valid:
# strings, numbers, tuples

# invalid:
# lists, booleans

user = {
  "name": "Felipe",
  "country": "Mexico",
  "age": 29,
  (1,2,3): "Something",
  (12.23, 43.12): "Ohio coords"
}

print(user)
print(user["name"])

user["name"] = 'Phil'
user["age"] = 10000
user["email"] = "a@a.com"
print(user)
