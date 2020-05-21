# from past.builtins import raw_input
# import datetime

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
#
# x = int(input())
# print(fact(x))

# n = int(raw_input())
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i * i
# print(d)

# import math
#
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
#
# print(', '.join(value))


# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
#
# x = int(input())
# print(fact(x))


# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         values.append(s)
# print(",".join(values))


# s = input()
# d = {"DIGITS": 0, "LETTERS": 0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"] += 1
#     elif c.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
#
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])


# a = input()
# n1 = int(f"{a}")
# n2 = int(f"{a}{a}")
# n3 = int("%s%s%s" % (a, a, a))
# n4 = int("%s%s%s%s" % (a, a, a, a))
# print(n1 + n2 + n3 + n4)


# values = input()
# numbers = [x for x in values.split(",") if int(x) % 2 != 0]
# print(",".join(numbers))


# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation == "D":
#         netAmount += amount
#     elif operation == "W":
#         netAmount -= amount
#     else:
#         pass
# print("Net amount is: ", netAmount)


# import re
#
# value = []
# items = [x for x in input().split(',')]
# for p in items:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", p):
#         continue
#     elif not re.search("[0-9]", p):
#         continue
#     elif not re.search("[A-Z]", p):
#         continue
#     elif not re.search("[$#@]", p):
#         continue
#     elif re.search("\s", p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))


# from operator import itemgetter, attrgetter
#
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
#
# print(sorted(l, key=itemgetter(0, 1, 2)))


# def put_numbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i += 1
#         if j % 7 == 0:
#             yield j
#
#
# print([i for i in put_numbers(100)])


# import math
#
# pos = [0, 0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction == "UP":
#         pos[0] += steps
#     elif direction == "DOWN":
#         pos[0] -= steps
#     elif direction == "LEFT":
#         pos[1] -= steps
#     elif direction == "RIGHT":
#         pos[1] += steps
#     else:
#         pass
#
# print("Position is: ", int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))


# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)


# def square(num):
#     '''Return the square value of the input number.
#
#     The input number must be integer. DUPA
#     '''
#     return num ** 2
#
#
# print(square(2))
# print(square.__doc__)


# class Person:
#     # Define the class parameter "name"
#     name = "Dupa"
#
#     def __init__(self, name):
#         # self.name is the instance parameter
#         self.name = name
#
#
# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))
#
# # nico = Person()
# # nico.name = "Nico"
# # print("%s name is %s" % (Person.name, nico.name))


# def print_dict():
#     d = {i: i ** 2 for i in range(1, 21)}
#     print(d)
#
#
# print_dict()
#
#
# def print_dict_2():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     print(d)
#
#
# print_dict_2()
#
#
# def print_dict_3():
#     d = {i: i ** 2 for i in range(1, 21)}
#     for (k, v) in d.items():
#         print(k, v)
#
#
# print_dict_3()
#


# def list_create():
#     li = [i ** 2 for i in range(1, 21)]
#     print(li)
#     print(li[0:100:2])
#     print(tuple(li))
#
#
# list_create()


# tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tp1 = tp[:5]
# tp2 = tp[5:]
# print(tp1)
# print(tp2)
#
#
# tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# li = [i for i in tp if i % 2 == 0]
# tp_new = tuple(li)
# print(li)
# print(tp_new)


# s = input()
# if s == "yes" or s == "YES" or s == "Yes":
#     print("Yes")
# else:
#     print("No")


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenNumbers = filter(lambda x: x % 2 == 0, li)
# print([i for i in evenNumbers])


# STATIC METHOD: Działa i na classie i na obiekcie!

# class American:
#
#     @staticmethod
#     def print_nationality():
#         print("America")
#
#
# anAmerican = American()
# anAmerican.print_nationality()
# American.print_nationality()
#
#
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     def area(self):
#         return self.radius**2*3.14
#
#
# aCircle = Circle(2)
# print(aCircle.area())


# class MyError(Exception):
#     """My own exception class
#
#     Attributes:
#         msg  -- explanation of the error
#     """
#
#     def __init__(self, msg):
#         self.msg = msg
#
#
# error = MyError("something wrong")
# print(error)


# def f(n):
#     if n == 0:
#         return 0
#     else:
#         return f(n - 1) + 100
#
#
# n = int(input())
# print(f(n))


# def even_generator(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1
#
#
# n = int(input())
# values = [str(i) for i in even_generator(n)]
# # for i in even_generator(n):
# #     values.append(str(i))
#
# print(",".join(values))


# def num_generator(n):
#     for i in range(n + 1):
#         if i % 5 == 0 and i % 7 == 0:
#             yield i
#
#
# n = int(input())
# values = [str(i) for i in num_generator(n)]
# print(",".join(values))


# li = [2, 4, 6, 8, 9]
# for i in li:
#     assert i % 2 == 0


# expression = input("Enter mathematic expression to evaluate: ")
# print(f"The result is: {eval(expression)}")


# import math
#
#
# def bin_search(li, element):
#     bottom = 0
#     top = len(li) - 1
#     index = -1
#     while top >= bottom and index == -1:
#         mid = int(math.floor((top + bottom) / 2.0))
#         if li[mid] == element:
#             index = mid
#         elif li[mid] > element:
#             top = mid - 1
#         else:
#             bottom = mid + 1
#
#     return index
#
#
# li = [2, 5, 7, 9, 11, 17, 222]
# print(bin_search(li, 11))
# print(bin_search(li, 12))
