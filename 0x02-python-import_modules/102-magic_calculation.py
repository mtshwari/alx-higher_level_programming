def magic_calculation(a, b):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
