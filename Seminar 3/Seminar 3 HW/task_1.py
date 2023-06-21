# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

hike = {
    'Петя': ('Палатка', 'Спальник', 'Фонарик', 'Газовая горелка', 'Тент'),
    'Иван': ('Палатка', 'Спальник', 'Тент', 'Перчатки', 'Спички'),
    'Кристина': ('Палатка', 'Спальник', 'Фонарик', 'Кружка', 'Спички'),
    'Андрей': ('Палатка', 'Спальник', 'Фонарик', 'Спички', 'Удочка')
}

all_items = set()
uniq_items_dict = {}
not_have_items_dict = {}

for friend in hike:
    uniq_items = set(hike[friend])
    not_have_items = set()
    for next_friend in hike:
        if next_friend != friend:
            uniq_items -= set(hike[next_friend])
            if not not_have_items:
                not_have_items |= (set(hike[next_friend]))
            else:
                not_have_items.intersection_update(set(hike[next_friend]))
    all_items |= set(hike[friend])
    uniq_items_dict[friend] = uniq_items
    not_have_items_dict[friend] = not_have_items - set(hike[friend])

print(f"Все предметы: {all_items}\n"
      f"Уникальные предметы: {uniq_items_dict}\n"
      f"Предметы которые есть у всех кроме одного: {not_have_items_dict}")
