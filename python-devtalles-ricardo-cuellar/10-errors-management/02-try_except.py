def divide_number():
  try:
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))

    result = a / b
    print(result)
    return result
  except ValueError as error:
    print("Invalid Number")
  except ZeroDivisionError as error:
    print("It cannot be divided by zero")
  except Exception as error:
    print(type(error))

divide_number()