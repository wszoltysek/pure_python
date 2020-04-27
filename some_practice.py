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

# def test_args(*args):
#     for arg in args:
#         print(arg)
#
#
# def test_kwargs(**kwargs):
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#
#
# art = "Alala"
# ama = "lalalla mama dwa"
# lama = [1, 2, 3, 4, "debug"]
# diction = {"ala": "pies", "magda": "kot", "1": "number", 1: "liczba", "lista": [1, "cos", 3]}
#
# print(test_args(art, ama, lama, diction))
# print(test_kwargs(nazwa="Han Solo", opis="smuggler"))


# SORTOWANIE:

# int_list_one = [1, 3, 7, 2, 42]
# int_list_two = [1, 0, 17, 34, 22, 3, 7, 2, 42]
#
# int_list_one.sort()
# sorted_list = sorted(int_list_two)
#
# print(int_list_one)
# print(sorted_list)


# SPŁASZCZANIE LISTY LIST:

list_of_one = [[1], [2], [3], [4], [8], [9], 1] # Ten przykład wywali błąd!
list_of_lists = [[180.0], [173.8], [164.2], [156.5], [147.2], [138.2]]
flattened = [val for sublist in list_of_lists for val in sublist]
flattened_one = [val for sublist in list_of_one for val in sublist]
print(flattened)
print(flattened_one)
