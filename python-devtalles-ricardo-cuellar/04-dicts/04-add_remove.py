
user = {
  "name": "Felipe",
  "age": 29,
  "greet": "Hola Mundo",
  "numbers": [1, 2, 3]
}


# copy
# copy dict to a new variable
user_copy = user.copy()
user_copy['age'] = 20
print(user)
print(user_copy)

# pop
# pop cannot delete the last property since we don't have any sort in keys
# we need to specify the key
user.pop("age")
print(user)

# popitem()
# is going to delete the last declared property (in the declaration order)
# this is our declaration, so is going to delete numbers
# user = {
#   "name": "Felipe",
#   "age": 29,
#   "greet": "Hola Mundo",
#   "numbers": [1, 2, 3]
# }
user.popitem()
print(user)



# .update()
# update by key and value as param
# if something don't exists is going to create a new key
# like upsert
user.update({'name': 'Kone'})
user.update({ 'cats': 1 })
print(user)



# append()
# this syntax says that
# if value don't exists, add the default value ([] in this case)
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
user['skills'].append('FastApi')
print(user)