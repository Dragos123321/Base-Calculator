def compare_int_numbers(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    if len1 < len2:
        return -1
    elif len2 < len1:
        return 1
    else:
        for i in range(len1):
            if number1[i] < number2[i]:
                return -1
            elif number1[i] > number2[i]:
                return 1

        return 0


def compare_fractional_numbers(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    if len1 < len2:
        diff = len2 - len1
        for i in range(diff):
            number1.append("0")
    elif len2 < len1:
        diff = len1 - len2
        for i in range(diff):
            number2.append("0")
    else:
        for i in range(len1):
            if number1[i] < number2[i]:
                return -1
            elif number1[i] > number2[i]:
                return 1

        return 0
