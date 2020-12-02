from Conversions.to_base_10 import to_base_10_real
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.parse_functions import parse_number


def division_op(number1, number2, base):
    if base == 10:
        return float(number1) / float(number2)
    else:

        real_num_1, fractional_num_1 = parse_number(number1)
        real_num_2, fractional_num_2 = parse_number(number2)

        if len(real_num_1) == 1 and len(fractional_num_1) == 0:
            to_div = real_num_1
            to_be_div_int = real_num_2
            to_be_div_fractional = fractional_num_2
        else:
            to_div = real_num_2
            to_be_div_int = real_num_1
            to_be_div_fractional = fractional_num_1

        if to_div == '0':
            raise ValueError("Cannot divide by 0")

        real_result, real_reminder = compute_integer_part(to_be_div_int, to_div, base)
        fractional_result = compute_fractional_part(to_be_div_fractional, to_div, base, real_reminder)

        result = real_result + "." + fractional_result

        return result


def compute_fractional_part(to_be_div_fractional, to_div, base, real_reminder):
    max_len = len(to_be_div_fractional)
    result = ""

    if len(to_div) != 1:
        raise ValueError("Invalid operand")
    else:
        if real_reminder != '0':
            num_to_div_str = real_reminder
        else:
            num_to_div_str = ""
        for i in range(max_len):
            num_to_div_str += to_be_div_fractional[i]
            if len(num_to_div_str) == 1:
                if get_number_from_character(to_be_div_fractional[i]) < get_number_from_character(to_div[0]):
                    if i != 0:
                        result += '0'
                    continue
            num_to_div = to_base_10_real(num_to_div_str, base)
            div = get_number_from_character(to_div[0])

            last_digit = num_to_div // div
            result = result + get_character_from_number(last_digit)
            if num_to_div % div != 0:
                num_to_div_str = get_character_from_number(num_to_div % div)
            else:
                num_to_div_str = ""

        if result[0] == '0':
            return '0'
        else:
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
            num_to_div = to_base_10_real(num_to_div_str, base)
            div = get_number_from_character(to_div[0])

            last_digit = num_to_div // div
            result = result + get_character_from_number(last_digit)
            if num_to_div % div != 0:
                num_to_div_str = get_character_from_number(num_to_div % div)
            else:
                num_to_div_str = ""

        if result == "":
            return '0', num_to_div_str
        else:
            return result, num_to_div_str
