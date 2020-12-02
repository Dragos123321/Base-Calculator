from Utilities.numberic_utilities import get_number_from_character


def compare_int_numbers(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    if len1 < len2:
        return -1
    elif len2 < len1:
        return 1
    else:
        for i in range(len1):
            if get_number_from_character(number1[i]) < get_number_from_character(number2[i]):
                return -1
            elif get_number_from_character(number1[i]) > get_number_from_character(number2[i]):
                return 1

        return 0


def compare_fractional_numbers(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    if len1 < len2:
        diff = len2 - len1
        for i in range(diff):
            number1 += "0"
    elif len2 < len1:
        diff = len1 - len2
        for i in range(diff):
            number2 += "0"

    for i in range(len1):
        if get_number_from_character(number1[i]) < get_number_from_character(number2[i]):
            return -1
        elif get_number_from_character(number1[i]) > get_number_from_character(number2[i]):
            return 1

    return 0
