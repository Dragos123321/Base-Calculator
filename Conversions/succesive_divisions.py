from Operations.division_function import compute_integer_part


def successive_divisions(number1, source_base, destination_base):
    quotient = number1
    result = ""
    while quotient != "0":
        quotient, reminder = compute_integer_part(quotient, destination_base, source_base)
        result += reminder

    result = result[::-1]
    return result
