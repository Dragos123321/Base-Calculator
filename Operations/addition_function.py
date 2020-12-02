from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.parse_functions import parse_number


def addition(number1, number2, base):
    if base == 10:
        return float(number1) + float(number2)
    else:
        real_num_1, fractional_num_1 = parse_number(number1)
        real_num_2, fractional_num_2 = parse_number(number2)

        fractional_result, reminder = compute_fractional_part(fractional_num_1, fractional_num_2, base)
        real_result = compute_integer_part(real_num_1, real_num_2, base, reminder)

        result = real_result + "." + fractional_result

        return result


def compute_fractional_part(fractional_num_1, fractional_num_2, base):
    reminder = 0

    if len(fractional_num_1) < len(fractional_num_2):
        aux = fractional_num_1
        fractional_num_1 = fractional_num_2
        fractional_num_2 = aux

    max_len = len(fractional_num_1)

    while len(fractional_num_2) < max_len:
        fractional_num_2.append("0")

    result = ""

    for i in range(max_len - 1, -1, -1):
        last_digit = (get_number_from_character(fractional_num_1[i]) +
                      get_number_from_character(fractional_num_2[i]) + reminder) % base
        result = result + get_character_from_number(last_digit)
        reminder = (get_number_from_character(fractional_num_1[i]) +
                    get_number_from_character(fractional_num_2[i]) + reminder) // base

    result = result[::-1]
    return result, reminder


def compute_integer_part(real_num_1, real_num_2, base, fractional_reminder):
    reminder = fractional_reminder

    if len(real_num_1) < len(real_num_2):
        aux = real_num_1
        real_num_1 = real_num_2
        real_num_2 = aux

    min_len = len(real_num_2)
    max_len = len(real_num_1)
    diff = max_len - min_len
    result = ""

    for i in range(min_len - 1, -1, -1):
        last_digit = (get_number_from_character(real_num_1[i + diff]) + get_number_from_character(real_num_2[i])
                      + reminder) % base
        result = result + get_character_from_number(last_digit)
        reminder = (get_number_from_character(real_num_1[i + diff]) + get_number_from_character(real_num_2[i])
                    + reminder) // base

    if max_len == min_len and reminder != 0:
        result = result + get_character_from_number(reminder)
    elif max_len > min_len:
        for i in range(max_len - min_len - 1, -1, -1):
            last_digit = (get_number_from_character(real_num_1[i]) + reminder) % base
            result = result + get_character_from_number(last_digit)
            reminder = (get_number_from_character(real_num_1[i]) + reminder) // base

    result = result[::-1]
    return result
