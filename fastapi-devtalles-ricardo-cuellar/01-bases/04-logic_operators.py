# and
age = 25
licensed = True

if age >= 18 and licensed:
  print("You can drive!")
  
  
# or
is_student = False
membership = True

if is_student or membership:
  print("Can have special price")
  
# not
is_admin = False

if not is_admin:
  print("Access denied")
  
# short circuiting
name = False
print(name and name.upper())