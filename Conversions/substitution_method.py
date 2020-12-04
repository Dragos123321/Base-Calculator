from Operations.operations import Operations
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


def convert_with_substitution(number, source_base, destination_base):
    for x in number:
        if get_number_from_character(x) >= source_base:
            raise ValueError("Invalid number in source base")

    result = "0"

    exp = len(number) - 1

    for digit in number:
        current_power = "1"
        for i in range(exp):
            current_power = Operations.multiplication(current_power, get_character_from_number(source_base),
                                                      destination_base)
        current_power = Operations.multiplication(current_power, digit, destination_base)
        result = Operations.addition(result, current_power, destination_base)
        exp -= 1

    return result
