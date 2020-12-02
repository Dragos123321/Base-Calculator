from Utilities.numberic_utilities import get_number_from_character
from Utilities.parse_functions import parse_number


def convert_with_substitution(source_base, destination_base, number_in_source_base):
    for x in number_in_source_base:
        if x != ",":
            if get_number_from_character(x) >= source_base:
                raise ValueError("Invalid number in source base")

    real_part_of_source, fractional_part_of_source = parse_number(number_in_source_base)

    exponent = 0
    length = len(number_in_source_base)
    real_part_of_destination = 0
    reminder = 0
    for i in range(length - 1, -1, -1):
        real_part_of_destination = real_part_of_destination +\
                                   get_number_from_character((get_number_from_character(real_part_of_source[i])
                                                              * pow(source_base, exponent) + reminder) % destination_base)
        reminder = (get_number_from_character(real_part_of_source[i]) * pow(source_base, exponent) + reminder)\
                   / destination_base
        exponent = exponent + 1

    number_in_destination_base = str(real_part_of_destination)
    # number_in_destination_base = float(number_in_destination_base)

    return number_in_destination_base
