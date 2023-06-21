# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from itertools import combinations

MAX_WEIGHT = 15

items = {
    "Палатка": 5,
    "Спальник": 1,
    "Топор": 2,
    "Спички": 0.02,
    "Котелок": 2,
    "Дрова": 15,
    "Вода": 5,
    "Верёвка": 2,
    "Фонарик": 0.5,
    "Карта": 0.2,
    "Удочка": 0.6,
    "Лодка": 20,
    "Еда": 12,
    "Инструменты": 7,
}

res = []

for i in range(len(items)):
    temp = []
    items_combinations = combinations(items, i)
    for combination in items_combinations:
        weight = 0
        for item in combination:
            weight += items[item]
        if weight <= MAX_WEIGHT:
            res.append(list(combination) + [weight])
for comb in res:
    print(comb)
