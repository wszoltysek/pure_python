# GENERATORY:


# def veoy(value):
#     sam_list = ["a", "b", "e", "y"]
#     for sam in value:
#         if sam in sam_list:
#             yield sam
#
#
# smt = "ala i ewelina ma kota"
#
# print([sam for sam in veoy(smt)])


# ARGS / KWARGS:

def test(*args, **kwargs):
    for arg in args:
        print(arg)


art = "Alala"
ama = "lalalla mama dwa"
lama = [1, 2, 3, 4, "debug"]
diction = {"ala": "pies", "magda": "kot", "1": "number", 1: "liczba", "lista": [1, "cos", 3]}

print(test(art, ama, lama, diction))
