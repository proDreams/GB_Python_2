# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

data = [1, 2, 3, 2, 76, 5, 8, 3, 6, 5, 2, 1, 5]
data_odd_index = []
data_odd_index2 = [i + 1 for i in range(len(data)) if data[i] % 2 != 0]

for i, item in enumerate(data, 1):
    if item % 2 != 0:
        data_odd_index.append(i)

print(data, data_odd_index, data_odd_index2, sep='\n')
