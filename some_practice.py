# GENERATORY:


def veoy(value):
    sam_list = ["a", "b", "e", "y"]
    for sam in value:
        if sam in sam_list:
            yield sam


smt = "ala i ewelina ma kota"

print([sam for sam in veoy(smt)])
