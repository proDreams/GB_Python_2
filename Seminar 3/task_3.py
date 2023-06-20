# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (1, 2, 2.5, 'adad', 2, 6, 'hello')
data_dict = {}

for item in data:
    data_dict.setdefault(type(item), [])
    data_dict[type(item)].append(item)

print(data_dict)
