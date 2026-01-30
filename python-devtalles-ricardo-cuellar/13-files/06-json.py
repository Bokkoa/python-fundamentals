import json

user = {
  'name': 'Felipe',
  'age': 29,
  'active': True
}

with open('data.json', 'w') as file:
  json.dump(user, file, indent=4)
  
with open('data.json', 'r') as file:
  data_read = json.load(file)
  print(data_read)
