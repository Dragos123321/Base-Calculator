from Utilities.comparison_functions import compare_int_numbers
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.to_base_10 import to_base_10


class Operations:
    @staticmethod
    def addition(number1, number2, base):
        if base == 10:
            return int(number1) + int(number2)
        else:

            reminder = 0

            if len(number1) < len(number2):
                aux = number1
                number1 = number2
                number2 = aux

            min_len = len(number2)
            max_len = len(number1)
            diff = max_len - min_len
            result = ""

            for i in range(min_len - 1, -1, -1):
                last_digit = (get_number_from_character(number1[i + diff]) + get_number_from_character(number2[i])
                              + reminder) % base
                result = result + get_character_from_number(last_digit)
                reminder = (get_number_from_character(number1[i + diff]) + get_number_from_character(number2[i])
                            + reminder) // base

            if max_len == min_len and reminder != 0:
                result = result + get_character_from_number(reminder)
            elif max_len > min_len:
                for i in range(max_len - min_len - 1, -1, -1):
                    last_digit = (get_number_from_character(number1[i]) + reminder) % base
                    result = result + get_character_from_number(last_digit)
                    reminder = (get_number_from_character(number1[i]) + reminder) // base

            result = result[::-1]

            return result

    @staticmethod
    def division_op(number1, number2, base):
        if base == 10:
            return int(number1) // int(number2)
        else:

            if number2 == '0':
                raise ValueError("Cannot divide by 0")

            max_len = len(number1)
            result = ""

            if len(number2) != 1:
                raise ValueError("Invalid operand")
            else:
                num_to_div_str = ""
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

                if num_to_div_str == "":
                    num_to_div_str = "0"

                if result == "":
                    return '0', num_to_div_str
                else:
                    return result, num_to_div_str

    @staticmethod
    def multiplication(number1, number2, base):
        if base == 10:
            return int(number1) * int(number2)
        else:

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

                if reminder != 0:
                    result += get_character_from_number(reminder)

                result = result[::-1]

                if result[0] == '0':
                    return '0'
                else:
                    return result

    @staticmethod
    def subtraction(number1, number2, base):
        if base == 10:
            return int(number1) - int(number2)
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
                elif max_len > min_len:
                    for i in range(max_len - min_len - 1, -1, -1):
                        if get_number_from_character(number1[i]) < reminder:
                            last_digit = get_number_from_character(number1[i]) + base - reminder
                            reminder = 1
                        else:
                            last_digit = get_number_from_character(number1[i]) - reminder
                            reminder = 0
                        result = result + get_character_from_number(last_digit)

                result = result[::-1]
                if result != "0":
                    result = result.lstrip("0")
                return result
