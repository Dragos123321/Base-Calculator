from Operations.division_function import compute_integer_part
from Utilities.numberic_utilities import get_character_from_number, get_number_from_character


def successive_divisions(number, source_base, destination_base):
    for x in number:
        if get_number_from_character(x) >= source_base:
            raise ValueError("Invalid number in source base")

    quotient = number
    result = ""
    destination_base = get_character_from_number(destination_base)
    while quotient != "0":
        quotient, reminder = compute_integer_part(quotient, destination_base, source_base)
        result += reminder

    result = result[::-1]
    return result
