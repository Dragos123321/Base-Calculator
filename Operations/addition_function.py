from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


def addition(number1, number2, base):
    if base == 10:
        return int(number1) + int(number2)
    else:

        result = compute_integer_part(number1, number2, base)

        return result


def compute_integer_part(real_num_1, real_num_2, base):
    reminder = 0

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
