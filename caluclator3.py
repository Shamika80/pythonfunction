def get_number():


 while True:
    try:
      number = float(input("Enter a number: "))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operation():

  while True:
    operation = input("Choose an operation (+, -, *, /): ").lower()
    if operation in ["+", "-", "*", "/"]:
      return operation
    else:
      print("Invalid operation. Please choose +, -, *, or /.")

def perform_calculation(num1, num2, operation):
  

  if operation == "+":
    return "add"(num1, num2)
  elif operation == "-":
    return "subtract"(num1, num2)
  elif operation == "*":
    return "multiply"(num1, num2)
  elif operation == "/":
    return "divide"(num1, num2)
  else:
    print("Error: Invalid operation.")
    return None


while True:
  num1 = get_number()
  num2 = get_number()

  operation = get_operation()

  result = perform_calculation(num1, num2, operation)

  if result is not None:
    print(f"The result is: {result}")
  else:
    print("An error occurred. Please try again.")

  choice = input("Do you want to perform another calculation? (y/n): ").lower()
  if choice != "y":
    break

print("Thank you for using the calculator!")