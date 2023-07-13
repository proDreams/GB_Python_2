import csv
import json
import os
from functools import wraps


def save_params(func):
    """ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл. """

    func_name = func.__name__
    if os.path.exists(f'out/{func_name}.json'):
        with open(f'out/{func_name}.json', 'r', encoding='utf-8') as j:
            result_list = json.load(j)
    else:
        result_list = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'args': args,
                  'kwargs': kwargs,
                  'result': func_res}
        result_list.append(result)
        with open(f'out/{func_name}.json', "w", encoding="utf-8") as j:
            json.dump(result_list, j, indent=2)
        return func_res

    return wrapper


def calculate(path):
    """ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла. """

    def deco(func):
        results = []

        def wrapper(*args, **kwargs):
            with open(path, 'r', encoding='utf-8', newline='') as c:
                csv_reader = csv.reader(c)
                for i, line in enumerate(csv_reader):
                    if i:
                        results.append(func(*map(int, line), **kwargs))
            return results

        return wrapper

    return deco
