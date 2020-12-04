import math

from Utilities.numberic_utilities import get_number_from_character, get_character_from_number


def rapid_conversions(number, source_base, destination_base):
    allowed_bases = [2, 4, 8, 16]
    if source_base not in allowed_bases or destination_base not in allowed_bases:
        raise ValueError("Invalid source base for rapid conversions")

    for x in number:
        if get_number_from_character(x) >= source_base:
            raise ValueError("Invalid number in source base")

    pow_2_source = int(math.log2(source_base))
    pow_2_destination = int(math.log2(destination_base))

    bits = []
    for i in range(len(number) - 1, -1, -1):
        digit = get_number_from_character(number[i])
        for j in range(pow_2_source):
            bits.append(digit % 2)
            digit //= 2

    while len(bits) % pow_2_destination != 0:
        bits.append(0)

    result = ""
    for i in range(0, len(bits), pow_2_destination):
        digit = get_character_from_number(sum([bits[i + j] * (1 << j) for j in range(pow_2_destination)]))
        result += digit

    result = result[::-1]

    return result
