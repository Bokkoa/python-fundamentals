# You will create a shopping cart with the following functionalities:
# Add product
# Remove product
# Show sorted list
# Search product
# Count products in cart
# Clear the cart

print("Shopping cart")

# Menu options
print("Options:")
print("1. Add product")
print("2. Remove product")
print("3. Show sorted list")
print("4. Search product")
print("5. Count products in cart")
print("6. Clear the cart")

shopping_cart = ["Laptop", "Glass", "Coffee", "Headphones"]

# Read user option
option = input("Choose an option (1-6): ")

if option == "1":
  new_product = input("Add the new product name: ")
  if new_product in shopping_cart:
    print("Product already added")
  else:
    shopping_cart.append(new_product)
    print("Product added!")
    print(shopping_cart)

elif option == "2":
  print(shopping_cart)
  product_index = input("Product index To remove: ")
  if product_index >= len(shopping_cart):
    print("Invalid index")
  else:
    shopping_cart.pop(product_index)

elif option == "3":
  sorted_list = shopping_cart[:]
  sorted_list.sort()
  print(sorted_list)

elif option == "4":
  search = input("Product To search: ")
  result = shopping_cart[search]
  print(f"Product {result} found in cart")

elif option == "5":
  result = shopping_cart.count()
  print(f"Products in cart: {result}")

elif option == "6":
  shopping_cart.clear()
  print("Car cleared!")

else:
  print("Invalid option")