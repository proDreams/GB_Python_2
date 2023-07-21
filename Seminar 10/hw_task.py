# Доработаем задачи 5-6.
# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from hw import fabric_class as f, classes as c

fish = c.Fish('Nemo', 3, 500)
new_fish = f.Fabric(c.Fish, 'Nemo1', 3, 500).do_copy()
print(new_fish)
