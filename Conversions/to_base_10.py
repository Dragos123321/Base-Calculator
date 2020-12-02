from Utilities.numberic_utilities import get_number_from_character


def to_base_10_real(number, base):
    number_in_base_10 = 0

    exp = len(number) - 1
    for digit in number:
        number_in_base_10 += get_number_from_character(digit) * pow(base, exp)
        exp -= 1

    return number_in_base_10
