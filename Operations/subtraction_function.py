from Utilities.comparison_functions import compare_int_numbers, compare_fractional_numbers
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


def subtraction(number1, number2, base):
    if base == 10:
        return int(number1) - int(number2)
    else:
        if compare_int_numbers(number1, number2) == -1:
            raise ValueError("The subtrahend is greater than minuend")

        result = compute_integer_part(number1, number2, base)

        return result


def compute_integer_part(real_num_1, real_num_2, base):
    reminder = 0
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
