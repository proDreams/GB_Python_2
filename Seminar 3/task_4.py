# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

data = [1, 2, 3, 2, 76, 5, 8, 3, 6, 5, 2, 1, 5]
print(data)
new_data = [i for i in data if data.count(i) != 2]
count = 2
for i in set(data):
    if data.count(i) == count:
        for _ in range(count):
            data.remove(i)

print(new_data)
