from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return n1 / n2
def exponent(n1, n2):
    return n1 ** n2
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "**" : exponent,
}
def get_valid_float(prompt):
    """Checks if the input is a valid float"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    keep_calculating = True
    print(logo)
    """Get num1 outside while loop so if user continues, the previous solution is used as num1"""
    num1 = get_valid_float("Enter the first number: ")

    while keep_calculating:
        for symbol in operations:
            print(symbol)
        operation = input("Select an operation. \n")
        if operation not in operations:
             print("This is not a valid selection")
             continue
        num2 = get_valid_float("Enter the second number: ")
        solution = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {solution}")
        if solution is None:
            keep_calculating = False
            print("\n" * 20)
            calculator()
        """Ask user if they want to continue with previous result. If not, restart calculator."""
        go_again = input(f"Do you want to continue with the previous result of {solution}? \n" 
                            "Type 'y' for yes and 'n' for no. \n").lower()
        if go_again == 'y':
           num1 = solution
        else:
           keep_calculating = False
           print("\n" * 20)
           calculator()

calculator()