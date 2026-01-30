
nested_dict = {
  "Person1": {
    "name": "Felipe",
    "age": 29,
    "city": "Mexico"
  },
  "Person2": {
    "name": "Vianey",
    "age": 23,
    "city": "Mexico"
  },
  "Person3": {
    "name": "Emi",
    "age": 19,
    "city": "Argentina"
  },
}

print(nested_dict)

for key, value in nested_dict.items():
  print(f"{key}: ")
  for sub_key, sub_value in value.items():
    print(f"{sub_key}: {sub_value}")