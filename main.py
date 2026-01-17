# BASIC CALCULATOR FUNCTIONS
# make user choose operation
            
# ADDITION FUNCTION
def add(x, y):
    return x + y

# SUBTRACTION FUNCTION
def sub (x, y):
    return x - y

# MULTIPLICATION FUNCTIONLK
def multiply (x, y):
    return x * y

# DIVISION FUNCTION
def divide (x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# loop back to make user choose operation again
while True:
    try: 
        x = int(input("Enter First Number: "))
        y = int(input("Enter second number: "))
    except: 
        print("Invalid, try again!")
        continue
    
    op = input("Enter operator (+, -, *, /): ")
    if op == "+":
        print("Result: \t", add(x, y))

    elif op == "-":
        print("Result: \t", sub(x, y))
    
    elif op == "*":
        print("Result: \t", multiply(x, y))

    elif op == "/":
        print("Result: \t", divide(x, y))

    else: print("Invalid operator!")

    # Ask user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed.")
        break

