from Conversions.substitution_method import convert_with_substitution
from Conversions.to_base_10 import to_base_10
from Utilities.numberic_utilities import get_number_from_character


def base_10_as_intermediate(number, source_base, destination_base):
    for x in number:
        if get_number_from_character(x) >= source_base:
            raise ValueError("Invalid number in source base")

    intermediate_in_base_10 = to_base_10(number, source_base)
    result = convert_with_substitution(str(intermediate_in_base_10), 10, destination_base)

    return result
