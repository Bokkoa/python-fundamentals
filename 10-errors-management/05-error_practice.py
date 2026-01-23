class InvalidAgeError(Exception):
  def __init__(self, age, message = "Age must be equal or greater than 18"):
    self.age = age
    self.message = message
    super().__init__(self.message)

class InvalidEmailError(Exception):
  def __init__(self, email, message = "Invalid email format"):
    self.email = email
    self.message = message
    super().__init__(self.message)

def register_user(name, age, email):
  if age < 18:
    # triggering our custom error
    raise InvalidAgeError(age)
  print(f"User {name} registered with {age} years old")
  
  if '@' not in email or '.' not in email.split("@")[-1]:
    raise InvalidEmailError(email)

try:
  register_user("Felipe", 28, 'a@a.com')
  register_user("Kone", 29, 'somemail')
except InvalidAgeError as e:
  print(f"Error: {e}")
except InvalidEmailError as e:
  print(f"Error: {e}")