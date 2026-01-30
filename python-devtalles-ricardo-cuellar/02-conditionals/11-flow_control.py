
age = int(input("Enter your age: "))
if age < 0:
  print("Invalid age")
elif age <= 12:
  print("Youre a kiddo")
elif age <= 17:
  print("Youre a teenager")
elif age <= 64:
  print("Youre an adult")
else:
  print("You are a senior man")