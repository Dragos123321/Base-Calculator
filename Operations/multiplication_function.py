from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


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

        result = compute_integer_part(to_be_mul_int, to_mul, base)

        return result


def compute_integer_part(to_be_mul_int, to_mul, base):
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
