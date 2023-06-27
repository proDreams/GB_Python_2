# Итераторы
# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter) # <list_iterator object at 0x0000020368475EA0>
# print(*list_iter) # 2 4 6 8
#
# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
#
# Генераторы
# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen)  # <generator object <genexpr> at 0x0000029E3B756260>
# for char in my_gen:
#     print(char)
#
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f"{len(x)=}\t{len(y)=}")
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f"{len(res)=}\n{res}")
#
# List Comprehensions
# my_listcomp = [chr(i) for i in range(97, 123)]
# print(my_listcomp)
# for char in my_listcomp:
#     print(char)
#
# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f"{res = }")
#
# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = [item for item in data if item % 2 == 0]
# print(f"{res = }")
#
# Генератор vs List comprehension
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f"{len(x)=}\t{len(y)=}")
# res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
# print(f"{len(res)=}\n{res}")
#
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# for item in mult:
#     print(f"{item = }")
#
# Генератор множеств
# my_setcomp = {chr(i) for i in range(97, 123)}
# print(my_setcomp)
# for char in my_setcomp:
#     print(char)
#
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f"{len(x)=}\t{len(y)=}")
# res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
# print(f"{len(res)=}\n{res}")
#
# Генератор словарей
# my_dictcomp = {i: chr(i) for i in range(97, 123)}
# print(my_dictcomp)
# for number, char in my_dictcomp.items():
#     print(f"dict[{number}] = {char}")

# Функция Факториала
# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n+1):
#         number *= i
#         result.append(number)
#     return result
#
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f"{i}! = {num}")

# Функции генераторы
# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f"{i}! = {num}")
