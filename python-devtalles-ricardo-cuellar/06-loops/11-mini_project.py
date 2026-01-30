inventory = {
    "chocolate": 10,
    "gummies": 5,
    "lollipop": 8,
    "gum": 2,
    "mexican_candy": 8,
    "cookie": 12
}

cart = []
print("Welcome to the candy store, DevCandy!")
print("Inventory:")

for index, candy in enumerate(inventory):
  print(f"{index} - {candy.capitalize()} ({inventory[candy]}$)")

print("Type Exit For program finalization.")

option = ""
while option != "exit":
  option = input("Enter an option to add to your cart: ").lower()
  
  if option not in inventory:
    print("Invalid option, try again!")
  else:
    cart.append(inventory[option])

print(f"You'll pay {sum(cart)} $, thanks for coming!")