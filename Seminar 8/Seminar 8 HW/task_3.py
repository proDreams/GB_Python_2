# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий. Соберите из созданных на уроке и в рамках
# домашнего задания функций пакет для работы с файлами разных форматов.
from task_3_module import work_with_files as wwf

wwf.generate_dict('C:\\Users\\proDream\\PycharmProjects\\GB_Python_2\\Seminar 8', './out')