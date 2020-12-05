from Utilities.numberic_utilities import get_number_from_character


def to_base_10(number, base):
    """
    Utility function to convert a number to base 10

    :param number: a number in base [base]
    :param base: the base of the number [number]
    :return: integer representing the number in base 10
    """

    number_in_base_10 = 0

    exp = len(number) - 1
    for digit in number:
        number_in_base_10 += get_number_from_character(digit) * pow(base, exp)
        exp -= 1

    return number_in_base_10
