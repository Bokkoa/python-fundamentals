
# Evaluate conditions

# And (everything should be true in order to get true)
print(True and True) # True
print(True and False) # False
print(False and False) # False

# Or (At least one value should be true)
print(True or True) # True
print(True or False) # True
print(False or False) # False

# Not (Deny an statement)
print(not True) # False
print(not False) # True

# And Example
age = 25
licensed = True
if age >= 18 and licensed:
  print("You can Drive")


# Or Example
is_student = False
membership = True
if is_student or membership:
  print("You can get an special disccount")

# Not example
is_admin = False
if not is_admin:
  print("Denied access")
