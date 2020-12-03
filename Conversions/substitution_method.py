from Utilities.numberic_utilities import get_number_from_character
from Utilities.parse_functions import parse_number


def convert_with_substitution(number, source_base, destination_base):
    for x in number:
        if get_number_from_character(x) >= source_base:
            raise ValueError("Invalid number in source base")

    result = 0

    exp = 0

    return exp
