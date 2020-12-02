import re


def parse_number(number):
    pos = number.find(".")
    if pos == -1:
        return number, '0'

    real = number[:pos]
    fractional = number[pos + 1:]

    return real, fractional


def parse_operation(operation):
    operand = re.findall('\+|\*|-|/', operation)
    if len(operand) != 1:
        raise ValueError("Invalid operation")
    else:
        parts = re.split('\+|\*|-|/', operation)

    parts = [p.strip(" ") for p in parts]

    parts[0] = parts[0].upper()
    parts[1] = parts[1].upper()

    return parts[0], operand, parts[1]
