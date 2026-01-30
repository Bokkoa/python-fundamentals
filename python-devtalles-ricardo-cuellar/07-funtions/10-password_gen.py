from random import randrange
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# characters = letters + numbers + symbols

# Simple formula: (item * 7 + 3) % len(characters)

# Input: 8
# Output: &D^#23SN

def password_generator(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    characters = letters + numbers + symbols

    password = ""
   
    for _ in range(length):
      rangom_char = randrange(len(characters))
      password += characters[rangom_char]
    return password


# Example usage
print(password_generator(8))
