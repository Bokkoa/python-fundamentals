class InvalidAgeError(Exception):
  def __init__(self, age, message = "Age must be equal or greater than 18"):
    self.age = age
    self.message = message
    super().__init__(self.message)

def register_user(name, age):
  if age < 18:
    # triggering our custom error
    raise InvalidAgeError(age)
  print(f"User {name} registered with {age} years old")

try:
  register_user("Felipe", 28)
  register_user("Kone", 16)
except InvalidAgeError as e:
  print(f"Error: {e}")