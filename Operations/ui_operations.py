from Conversions.succesive_divisions import successive_divisions
from Operations.addition_function import addition
from Operations.division_function import division_op
from Operations.multiplication_function import multiplication
from Operations.subtraction_function import subtraction
from Utilities.parse_functions import parse_operation
import traceback


def ui_menu():
    print("\nOptions Menu:")
    print("1 - insert operation")
    print("2 - insert conversion")
    print("x - exit application")


def ui_menu_operations():
    done = False

    available_commands = ["1", "2"]

    while not done:
        ui_menu()
        command = input("command> ")

        if command == "x":
            done = True
            print("Application exit")
        elif command not in available_commands:
            print("Invalid command")
        else:
            if command == "1":
                base = input("Base: ")
                operation = input("Insert operations: ")
                base = int(base)

                number1, operand, number2 = parse_operation(operation)

                result = ""

                try:
                    if operand[0] == "+":
                        result = addition(number1, number2, base)
                    if operand[0] == "-":
                        result = subtraction(number1, number2, base)
                    if operand[0] == "*":
                        result = multiplication(number1, number2, base)
                    if operand[0] == "/":
                        result = division_op(number1, number2, base)
                except ValueError as ve:
                    print(ve)
                    # traceback.print_exc()

                print(result)
            else:
                print(successive_divisions("3466", 8, "5"))
