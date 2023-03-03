

#add
def add(num_1, num_2):
    return num_1 + num_2


#subtract
def subtract(num_1, num_2):
    return num_1 - num_2


#multiply
def multiply(num_1, num_2):
    return num_1 * num_2


#divide
def divide(num_1, num_2):
    return num_1 / num_2


operations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
        }

def calculator():
    num_1 = float(input("enter number: "))

    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:

        operator_sign = input("pick an operation perform: ")

        num_2 = float(input("enter next number: "))

        calculation_function = operations[operator_sign]
        answer = calculation_function(num_1, num_2)


        print(f"{num_1} {operator_sign} {num_2} = {answer}")

        continuation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")

        if continuation == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()
    ##    operator_sign = input("pick an operation perform: ")
    ##    num_3 = int(input("enter next number: "))
    ##    calculation_function = operations[operator_sign]
    ##    new_answer = calculation_function(answer, num_3)
    ##
    ##
    ##    print(f"{answer} {operator_sign} {num_3} = {new_answer}")
    ##
    ##

calculator()
