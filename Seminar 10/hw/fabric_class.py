from . import classes as c


class Fabric:
    @staticmethod
    def create_obj(obj_type, name, age, feature):
        match obj_type.lower():
            case 'fish':
                return c.Fish(name, age, feature)
            case 'bird':
                return c.Bird(name, age, feature)
            case 'mammal':
                return c.Mammals(name, age, feature)
            case _:
                return "Такого класса нет"