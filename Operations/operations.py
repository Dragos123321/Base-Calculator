from Utilities.comparison_functions import compare_int_numbers
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.to_base_10 import to_base_10


class Operations:
    @staticmethod
    def addition(number1, number2, base):
        """
        This function performs the addition of two numbers ([number1] and [number2])
        in base [base]

        :param number1: a string representing the first number in base [base]
        :param number2: a string representing the second number in base [base]
        :param base: the base in which the numbers are represented and the addition is done
        :return: a string representing the sum of [number1] and [number2]
        """
        if base == 10:                                   # if the numbers are in base 10 we do
            return str(int(number1) + int(number2))           # the normal addition of two numbers in base 10
        else:

            reminder = 0

            if len(number1) < len(number2):              # compare the length of the numbers
                aux = number1                            # and put the longest in number1
                number1 = number2
                number2 = aux

            min_len = len(number2)
            max_len = len(number1)
            diff = max_len - min_len
            result = ""

            # go through the numbers from last digit to the first digit of the shortest and do the addition
            for i in range(min_len - 1, -1, -1):
                last_digit = (get_number_from_character(number1[i + diff]) + get_number_from_character(number2[i])
                              + reminder) % base
                result = result + get_character_from_number(last_digit)
                reminder = (get_number_from_character(number1[i + diff]) + get_number_from_character(number2[i])
                            + reminder) // base

            # if the numbers had the same length we put the reminder as the first digit if it is not 0
            if max_len == min_len and reminder != 0:
                result = result + get_character_from_number(reminder)

            # if they had not the same length we add the digits of the longest and add the reminder to them
            elif max_len > min_len:
                for i in range(max_len - min_len - 1, -1, -1):
                    last_digit = (get_number_from_character(number1[i]) + reminder) % base
                    result = result + get_character_from_number(last_digit)
                    reminder = (get_number_from_character(number1[i]) + reminder) // base

            # reverse the digits of the result to obtain the correct number
            result = result[::-1]

            return result

    @staticmethod
    def division_op(number1, number2, base):
        """
        This function performs the division of two numbers ([number1] and [number2])
        in base [base]

        :param number1: a string representing the first number in base [base]
        :param number2: a string representing the second number in base [base] having one digit
        :param base: the base in which the numbers are represented and the division is done
        :return: two strings representing the quotient and reminder of the division between [number1] and [number2]

        Raises a ValueError if [number2] if 0 or if is has more than one digit
        """
        if number2 == '0':
            raise ValueError("Cannot divide by 0")
        if len(number2) != 1:
            raise ValueError("Invalid operand")

        if base == 10:
            return str(int(number1) // int(number2)), str(int(number1) % int(number2))
        else:
            max_len = len(number1)
            result = ""

            num_to_div_str = ""

            # we do the division looping through the number
            for i in range(max_len):
                num_to_div_str += number1[i]
                if len(num_to_div_str) == 1:
                    if get_number_from_character(number1[i]) < get_number_from_character(number2[0]):
                        if i != 0:
                            result += '0'
                        continue
                num_to_div = to_base_10(num_to_div_str, base)
                div = get_number_from_character(number2[0])

                last_digit = num_to_div // div
                result = result + get_character_from_number(last_digit)
                if num_to_div % div != 0:
                    num_to_div_str = get_character_from_number(num_to_div % div)
                else:
                    num_to_div_str = ""

            # if the reminder is "" then it is 0
            if num_to_div_str == "":
                num_to_div_str = "0"

            # if the result is "" we return 0
            if result == "":
                return '0', num_to_div_str
            else:
                return result, num_to_div_str

    @staticmethod
    def multiplication(number1, number2, base):
        """
        This function performs the multiplication of two numbers ([number1] and [number2])
        in base [base]

        :param number1: a string representing the first number in base [base]
        :param number2: a string representing the second number in base [base] having one digit
        :param base: the base in which the numbers are represented and the multiplication is done
        :return: two strings representing product of [number1] and [number2]

        Raises a ValueError if [number2] is 0 or if is has more than one digit
        """
        if base == 10:
            return str(int(number1) * int(number2))
        else:
            # find the number having one digit
            if len(number1) == 1 and len(number2) > 1:
                to_mul = number1
                to_be_mul_int = number2
            else:
                to_mul = number2
                to_be_mul_int = number1

            reminder = 0

            max_len = len(to_be_mul_int)
            result = ""

            if len(to_mul) != 1:
                raise ValueError("Invalid operand")
            else:
                for i in range(max_len - 1, -1, -1):
                    last_digit = (get_number_from_character(to_be_mul_int[i]) * get_number_from_character(to_mul[0])
                                  + reminder) % base
                    result = result + get_character_from_number(last_digit)
                    reminder = (get_number_from_character(to_be_mul_int[i]) * get_number_from_character(to_mul[0])
                                + reminder) // base

                # if the reminder is not 0 then we add it at the beginning of the result
                if reminder != 0:
                    result += get_character_from_number(reminder)

                # reverse the digits to get the correct number
                result = result[::-1]

                if result[0] == '0':
                    return '0'
                else:
                    return result

    @staticmethod
    def subtraction(number1, number2, base):
        """
        This function performs the subtraction of two numbers ([number1] and [number2])
        in base [base]

        :param number1: a string representing the first number in base [base]
        :param number2: a string representing the second number in base [base]
        :param base: the base in which the numbers are represented and the subtraction is done
        :return: two strings representing difference between [number1] and [number2]

        Raises a ValueError if [number2] is greater than [number1]
        """
        if base == 10:
            return str(int(number1) - int(number2))
        else:
            if compare_int_numbers(number1, number2) == -1:
                raise ValueError("The subtrahend is greater than minuend")

            reminder = 0

            if len(number1) < len(number2):
                raise ValueError("The subtrahend is greater than minuend")
            else:
                min_len = len(number2)
                max_len = len(number1)
                diff = max_len - min_len
                result = ""

                # go through the numbers from last digit to the first digit of the shortest and do the subtraction
                for i in range(min_len - 1, -1, -1):
                    minuend = get_number_from_character(number1[i + diff])
                    sub = get_number_from_character(number2[i])
                    if minuend < sub + reminder:
                        last_digit = minuend + base - sub - reminder
                        reminder = 1
                    else:
                        last_digit = minuend - sub - reminder
                        reminder = 0
                    result = result + get_character_from_number(last_digit)

                if max_len == min_len and reminder != 0:
                    result = result + get_character_from_number(reminder)
                # if the first number is longer than the second we put its digits athe the beginning
                # of the result subtracting the reminder
                elif max_len > min_len:
                    for i in range(max_len - min_len - 1, -1, -1):
                        if get_number_from_character(number1[i]) < reminder:
                            last_digit = get_number_from_character(number1[i]) + base - reminder
                            reminder = 1
                        else:
                            last_digit = get_number_from_character(number1[i]) - reminder
                            reminder = 0
                        result = result + get_character_from_number(last_digit)

                # reverse the digits to get the correct number
                result = result[::-1]
                if result != "0":
                    result = result.lstrip("0")
                return result
