from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.parse_functions import parse_number


def multiplication(number1, number2, base):
    if base == 10:
        return float(number1) * float(number2)
    else:

        real_num_1, fractional_num_1 = parse_number(number1)
        real_num_2, fractional_num_2 = parse_number(number2)

        if len(real_num_1) == 1 and len(fractional_num_1) == 0:
            to_mul = real_num_1
            to_be_mul_int = real_num_2
            to_be_mul_fractional = fractional_num_2
        else:
            to_mul = real_num_2
            to_be_mul_int = real_num_1
            to_be_mul_fractional = fractional_num_1

        fractional_result, fractional_reminder = compute_fractional_part(to_be_mul_fractional, to_mul, base)
        real_result = compute_integer_part(to_be_mul_int, to_mul, base, fractional_reminder)

        result = real_result + "." + fractional_result

        return result


def compute_fractional_part(to_be_mul_fractional, to_mul, base):
    reminder = 0

    max_len = len(to_be_mul_fractional)
    result = ""

    for i in range(max_len - 1, -1, -1):
        last_digit = (get_number_from_character(to_be_mul_fractional[i]) *
                      get_number_from_character(to_mul[0])
                      + reminder) % base
        result = result + get_character_from_number(last_digit)
        reminder = (get_number_from_character(to_be_mul_fractional[i]) * get_number_from_character(to_mul[0])
                    + reminder) // base

    if reminder != 0:
        result += get_character_from_number(reminder)

    result = result[::-1]

    if result[0] == '0':
        return '0', 0
    else:
        return result, reminder


def compute_integer_part(to_be_mul_int, to_mul, base, fractional_reminder):
    reminder = fractional_reminder

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
