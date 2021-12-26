from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0.0:
        return "Divide by 0 Error"
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        if answer == "Divide by 0 Error":
            print(answer)
            choice = input("Type 'new' to start a new calculation, 'exit' to exit \n")
        else:
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            choice = input(f"'y' to continue calculating with {answer}, 'new' for new calculation, 'exit' to exit \n")
        if choice == 'y':
            num1 = answer
        elif choice == 'new':
            calculator()
        else:
            should_continue = False


# Start the program
calculator()
