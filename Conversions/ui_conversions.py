from Conversions.substitution_method import convert_with_substitution


def ui_menu_conversions():
    source_base = input("Source Base: ")
    destination_base = input("Destination Base: ")
    number_in_source_base = input("Number in source base: ")

    source_base = int(source_base)
    destination_base = int(destination_base)

    if source_base < destination_base:
        number_in_destination_base = convert_with_substitution(source_base, destination_base, number_in_source_base)

    print("Number in destinations base is: ")
    print(number_in_destination_base)
