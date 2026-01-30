tax = 16
other_tax = 16
# this is assigned but not changed
def change_global():
  tax = 18
  global other_tax # Global declaration required for mutability
  other_tax = 18 # ACTUALLY CHANGED in the global scope
  return tax

print(change_global()) # 18
print(tax) # 16
print(other_tax) # 18