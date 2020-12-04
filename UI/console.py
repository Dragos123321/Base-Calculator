from Conversions.rapid_conversions import rapid_conversions
from Conversions.substitution_method import convert_with_substitution
from Conversions.succesive_divisions import successive_divisions
from Conversions.to_base_10 import to_base_10
from Operations.operations import Operations


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
                    base = input("Base: ")
                    base = int(base)

                    number1, operand, number2 = [input("First number: ").strip(), input("Operator: ").strip(),
                                                 input("Second Number: ").strip()]
                    number1 = number1.upper()
                    number2 = number2.upper()

                    if operand[0] not in available_operands:
                        print(f"Operator {operand[0]} is invalid")
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
                        source_base = int(input("Source base: "))
                        destination_base = int(input("Destination base: "))
                        number = input("Number: ")
                        number = number.upper()

                        rapid_bases = [2, 4, 8, 16]

                        if destination_base == 10:
                            result = to_base_10(number, source_base)
                            print(result)
                        elif source_base in rapid_bases and destination_base in rapid_bases:
                            result = rapid_conversions(number, source_base, destination_base)
                            print(result)
                        elif source_base > destination_base:
                            result = successive_divisions(number, source_base, destination_base)
                            print(result)
                        else:
                            result = convert_with_substitution(number, source_base, destination_base)
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
