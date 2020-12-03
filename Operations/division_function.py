from Conversions.to_base_10 import to_base_10
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


def division_op(number1, number2, base):
    if base == 10:
        return int(number1) // int(number2)
    else:

        if number2 == '0':
            raise ValueError("Cannot divide by 0")

        result, real_reminder = compute_integer_part(number1, number2, base)

        return result


def compute_integer_part(to_be_div_int, to_div, base):
    max_len = len(to_be_div_int)
    result = ""

    if len(to_div) != 1:
        raise ValueError("Invalid operand")
    else:
        num_to_div_str = ""
        for i in range(max_len):
            num_to_div_str += to_be_div_int[i]
            if len(num_to_div_str) == 1:
                if get_number_from_character(to_be_div_int[i]) < get_number_from_character(to_div[0]):
                    if i != 0:
                        result += '0'
                    continue
            num_to_div = to_base_10(num_to_div_str, base)
            div = get_number_from_character(to_div[0])

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
