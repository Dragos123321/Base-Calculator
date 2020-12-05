from Utilities.numberic_utilities import get_number_from_character


def compare_int_numbers(number1, number2):
    """
    Compares two numbers in the same base

    :param number1: a string representing a number
    :param number2: a string representing a number
    :return: -1 if the second number is bigger, 0 if they are equal, 1 if the first number is bigger
    """
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
