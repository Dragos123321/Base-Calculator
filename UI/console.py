from Conversions.conversions import Conversions
from Operations.operations import Operations
from Utilities.to_base_10 import to_base_10


class Console:
    @staticmethod
    def run():
        """
        The main loop of the application.
        It handles the input and the exceptions that appear during the execution

        :return:
        """
        done = False

        available_commands = ["1", "2"]
        available_operands = ["+", "-", "*", "/"]

        while not done:
            Console.ui_menu()
            command = input("command> ")

            if command == "x":
                done = True
                print("Application exit")
            elif command not in available_commands:
                print("Invalid command")
            else:
                if command == "1":
                    base = input("Base [2-16]: ")
                    base = int(base)

                    number1, operand, number2 = [input(f"First number base {base}: ").strip(),
                                                 input("Operator [+, -, *, /]: ").strip(),
                                                 input(f"Second Number {base}: ").strip()]
                    number1 = number1.upper()
                    number2 = number2.upper()

                    if operand[0] not in available_operands:
                        print(f"Operator {operand[0]} is invalid")
                    elif base not in range(2, 17):
                        print("The base is not in range [2-16]")
                    else:
                        result = ""
                        try:
                            if operand[0] == "+":
                                result = Operations.addition(number1, number2, base)
                            if operand[0] == "-":
                                result = Operations.subtraction(number1, number2, base)
                            if operand[0] == "*":
                                result = Operations.multiplication(number1, number2, base)
                            if operand[0] == "/":
                                result, reminder = Operations.division_op(number1, number2, base)
                        except ValueError as ve:
                            print(ve)

                        print(result)
                else:
                    try:
                        source_base = int(input("Source base [2-16]: "))
                        destination_base = int(input("Destination base [2-16]: "))
                        number = input("Number: ")
                        number = number.upper()

                        rapid_bases = [2, 4, 8, 16]

                        if source_base not in range(2, 17) or destination_base not in range(2, 17):
                            print("The base is not in range [2-16]")
                        elif destination_base == 10:
                            result = to_base_10(number, source_base)
                            print(result)
                        elif source_base in rapid_bases and destination_base in rapid_bases:
                            result = Conversions.rapid_conversions(number, source_base, destination_base)
                            print(result)
                        elif source_base > destination_base:
                            result = Conversions.successive_divisions(number, source_base, destination_base)
                            print(result)
                        else:
                            result = Conversions.substitution_method(number, source_base, destination_base)
                            print(result)
                    except ValueError as ve:
                        print(ve)

    @staticmethod
    def ui_menu():
        """
        This function prints the options menu

        :return:
        """
        print("\nOptions Menu:")
        print("1 - insert operation")
        print("2 - insert conversion")
        print("x - exit application")
