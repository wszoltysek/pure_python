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


# import random

# print(random.random() * 100)
# print(random.choice([i for i in range(0, 1056) if i % 5 == 0 and i % 7 == 0]))
# print(random.sample([i for i in range(100, 200)], 5))
# print(random.sample(range(100, 200), 6))
# print(random.sample([i for i in range(100, 200) if i % 2 == 0], 5))
# print(random.randrange(5, 7))


# from timeit import Timer
#
# t = Timer("for i in range(100):1+1")
# print(t.timeit())


# import random
#
# li = [3, 6, 7, 8]
# random.shuffle(li)
# print(li)
# print(random.shuffle(li)) # TO ZWRÓCI NONE ! Tak samo jak z sort i sorted !!!


# subjects = ["I", "You"]
# verbs = ["Play", "Love"]
# objects = ["Hockey", "Football"]
#
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence = f"{subjects[i]} {verbs[j]} {objects[k]}."
#             print(sentence)


# li = [12, 24, 35, 70, 88, 120, 155]
# li_new = [i for i in li if i % 5 != 0 and i % 7 != 0]
# print(li_new)


# li = [12, 24, 35, 70, 88, 120, 155]
# print(li)
# li = [x for (i, x) in enumerate(li) if i % 2 != 0]
# print(li)


# li = [12, 24, 35, 70, 88, 120, 155]
# print(li)
# li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
# print(li)


# array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)


# set1 = set([1, 3, 6, 78, 35, 55])
# set2 = set([12, 24, 35, 24, 88, 120, 155])
# set1 &= set2
# set1 = set1 & set2 # TO SAMO CO &= !!!
# li = list(set1)
# print(li)


# def remove_duplicate(li):
#     newli = []
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add(item)
#             newli.append(item)
#     return newli
#
#
# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# print(remove_duplicate(li))


# Count char in string. Output as a dict:

# dic = {}
# s = input()
# for i in s:
#     dic[i] = dic.get(i, 0) + 1
# print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))


# Reverse string:

# s = input()
# rev_s = s[::-1]
# print(rev_s)


# Permutations - wszystkie możliwe kombinacje zbioru skończonego:

# import itertools
#
# print(list(itertools.permutations([1, 2, 3])))


# def solve(numheads, numlegs):
#     ns = 'No solutions!'
#     for i in range(numheads + 1):
#         j = numheads - i
#         if 2 * i + 4 * j == numlegs:
#             return i, j
#     return ns, ns
#
#
# numheads = 35
# numlegs = 94
# solutions = solve(numheads, numlegs)
# print(solutions)


# EXTRAS:

class Reverse:
    def __init__(self, value):
        self.value = value

    def reverse(self):
        # return self.value[::-1]
        return ' '.join(reversed(value.split()))


value = input()
print(Reverse(value).reverse())


class PrintString:
    def __init__(self):
        self.value = ""

    def get_string(self):
        self.value = input()

    def print_string(self):
        print(self.value.upper())


string = PrintString()
string.get_string()
string.print_string()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


try:
    width = int(input("Enter width: "))
    length = int(input("Enter lenght: "))

    rect = Rectangle(length, width)
    print(f"Area have {rect.compute_area()} square meters.")

except ValueError:
    print("Incorrect input. Must be int!")


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        return 2 * math.pi * self.radius


try:
    radius = int(input("Enter radius in meteres: "))

    rect = Circle(radius)
    print(f"Circle have {round(rect.compute_area())} square meters.")
    print(f"Circle perimeter equales {rect.compute_perimeter()} meters.")

except ValueError:
    print("Incorrect input. Must be int!")