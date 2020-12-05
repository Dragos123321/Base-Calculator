import math

from Operations.operations import Operations
from Utilities.numberic_utilities import get_number_from_character, get_character_from_number
from Utilities.to_base_10 import to_base_10


class Conversions:
    @staticmethod
    def rapid_conversions(number, source_base, destination_base):
        """
        It converts a number from base [source_base] in base [destination_base] using the
        rapid conversions algorithm.

        :param number: string representing number in base [source_base]
        :param source_base:  the source base [2, 4, 8, or 16]
        :param destination_base: the destination base [2, 4, 8, or 16]
        :return: converted number

        Raises ValueError if the bases are not [2, 4, 8 or 16] or if the number contains digits >= than the source_base
        """
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

    @staticmethod
    def substitution_method(number, source_base, destination_base):
        """
        It converts a number from base [source_base] in base [destination_base] using the
        substitution algorithm.

        :param number: string representing number in base [source_base]
        :param source_base:  the source base [2-16]
        :param destination_base: the destination base [2-16]
        :return: converted number

        Raises ValueError if the number contains digits >= than the source_base
        """
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

    @staticmethod
    def successive_divisions(number, source_base, destination_base):
        """
        It converts a number from base [source_base] in base [destination_base] using the
        successive divisions algorithm.

        :param number: string representing number in base [source_base]
        :param source_base:  the source base
        :param destination_base: the destination base
        :return: converted number

        Raises ValueError if the number contains digits >= than the source_base
        """
        for x in number:
            if get_number_from_character(x) >= source_base:
                raise ValueError("Invalid number in source base")

        quotient = number
        result = ""
        destination_base = get_character_from_number(destination_base)
        while quotient != "0":
            quotient, reminder = Operations.division_op(quotient, destination_base, source_base)
            result += reminder

        result = result[::-1]
        return result

    @staticmethod
    def base_10_as_intermediate(number, source_base, destination_base):
        """
        It converts a number from base [source_base] in base [destination_base] using
        base 10 as intermediate base.

        :param number: string representing number in base [source_base]
        :param source_base:  the source base
        :param destination_base: the destination base
        :return: converted number

        Raises ValueError if the number contains digits >= than the source_base
        """
        for x in number:
            if get_number_from_character(x) >= source_base:
                raise ValueError("Invalid number in source base")

        intermediate_in_base_10 = to_base_10(number, source_base)
        if destination_base > 10:
            result = Conversions.substitution_method(str(intermediate_in_base_10), 10, destination_base)
        else:
            result = Conversions.successive_divisions(str(intermediate_in_base_10), 10, destination_base)

        return result

