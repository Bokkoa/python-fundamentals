def divide_number():
  try:
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))
    result = a / b
    
  except ValueError as error:
    print("Invalid Number")
  except ZeroDivisionError as error:
    print("It cannot be divided by zero")
  except Exception as error:
    print(type(error))
  
  # Only is going to be executed if everything else was good
  else:
    print(result)
    return result
  
  # Is going to be executed wheter it fails or not
  finally:
    print("Thanks for use our calculator")

divide_number()