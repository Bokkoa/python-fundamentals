try:
  with open("restricted_file.txt", 'r') as file:
    content = file.read()
except FileNotFoundError:
  print("File doens't exists!")
except PermissionError:
  print("You don't have permission to open this file")
except Exception as err:
  print(f"Something happened: {err}")