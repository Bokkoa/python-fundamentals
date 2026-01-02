# Concatenation
name = 'Felipe'
last_name = 'Cruz'

# full_name = name + ' ' + last_name # <- Bad practice hardcoding a space

age = 28

full_name = f'{name} {last_name}'

message = f'{full_name} you\'re {age}'
print(full_name)
print(message)