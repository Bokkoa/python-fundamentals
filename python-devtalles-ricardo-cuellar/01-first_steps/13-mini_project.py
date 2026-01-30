# Register
# Get name, birth, email and pwd dinamically

"""
  Name: Felipe
  Email: felipe@something.com
  You will be N years old in 2050
  Your password is: **** <- asterisk should be dynamic
"""

name = input("Enter your name: ")
email = input("Enter your email: ")
birthyear = int(input("Enter your year of birth: "))
password = input("Enter your password: ")

age = 2050 - birthyear
formatted_password = "*" * len(password)

print(f'''
      Name: {name}
      Email: {email}
      Your will be {age} years old in 2050
      Your password is: {formatted_password}
      ''')