from Utilities.comparison_functions import compare_int_numbers, compare_fractional_numbers
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.parse_functions import parse_number


def subtraction(number1, number2, base):
    if base == 10:
        return float(number1) - float(number2)
    else:
        real_num_1, fractional_num_1 = parse_number(number1)
        real_num_2, fractional_num_2 = parse_number(number2)

        if compare_int_numbers(real_num_1, real_num_2) == -1:
            raise ValueError("The subtrahend is greater than minuend")
        elif compare_int_numbers(real_num_1, real_num_2) == 0 \
                and compare_fractional_numbers(fractional_num_1, fractional_num_2) == -1:
            raise ValueError("The subtrahend is greater than minuend")

        fractional_result, fractional_reminder = compute_fractional_part(fractional_num_1, fractional_num_2, base)
        integer_result = compute_integer_part(real_num_1, real_num_2, base, fractional_reminder)

        result = integer_result + "." + fractional_result

        return result


def compute_fractional_part(fractional_num_1, fractional_num_2, base):
    reminder = 0

    max_len = len(fractional_num_1)
    result = ""

    while len(fractional_num_2) < max_len:
        fractional_num_2 += "0"

    for i in range(max_len - 1, -1, -1):
        minuend = get_number_from_character(fractional_num_1[i])
        sub = get_number_from_character(fractional_num_2[i])
        if minuend < sub + reminder:
            last_digit = minuend + base - sub - reminder
            reminder = 1
        else:
            last_digit = minuend - sub - reminder
            reminder = 0
        result = result + get_character_from_number(last_digit)

    result = result[::-1]
    result = result.rstrip("0")
    return result, reminder


def compute_integer_part(real_num_1, real_num_2, base, fractional_reminder):
    reminder = fractional_reminder
    print(reminder)

    if len(real_num_1) < len(real_num_2):
        raise ValueError("The subtrahend is greater than minuend")
    else:
        min_len = len(real_num_2)
        max_len = len(real_num_1)
        diff = max_len - min_len
        result = ""

        for i in range(min_len - 1, -1, -1):
            minuend = get_number_from_character(real_num_1[i + diff])
            sub = get_number_from_character(real_num_2[i])
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
                if get_number_from_character(real_num_1[i]) < reminder:
                    last_digit = get_number_from_character(real_num_1[i]) + base - reminder
                    reminder = 1
                else:
                    last_digit = get_number_from_character(real_num_1[i]) - reminder
                    reminder = 0
                result = result + get_character_from_number(last_digit)

        result = result[::-1]
        if result != "0":
            result = result.lstrip("0")
        return result
