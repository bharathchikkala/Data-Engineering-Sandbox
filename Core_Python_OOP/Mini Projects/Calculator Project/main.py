import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4, 8))
condition2 = True
while condition2:
    number1 = int(input("Enter a number: "))
    condition = True
    while condition:
        for symbol in operations:
            print(symbol)
        operator = input("Enter a operator: ")
        if operator not in operations:
            print("Invalid operator")
        number2 = int(input("Enter another number: "))
        result = operations[operator](number1, number2)
        print(f"{number1} {operator} {number2} = {result}")
        next_also = input(f"u want to continue operation with {result} number type yes or no: ")
        if next_also == "yes":
            number1 = result
        else:
            condition = False
            print("\n" * 20)
            condition2 = True

