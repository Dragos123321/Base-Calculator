def get_number_from_character(character):
    digits = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, "I": 18, 'J': 19, "K": 20}

    if '0' <= character <= '9':
        return int(character)
    elif character in digits:
        return digits[character]
    else:
        raise ValueError(f"Invalid character {character}")


def get_character_from_number(number):
    digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: "I", 19: 'J', 20: "K"}

    if 0 <= number <= 9:
        return str(number)
    elif number in digits:
        return digits[number]
    else:
        raise ValueError("Invalid number")
