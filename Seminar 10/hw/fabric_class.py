from . import classes as c


class Fabric:
    def __init__(self, obj: c.Fish):
        self.obj = obj

    def do_copy(self):
        return self.obj.__class__(self.obj.name, self.obj.age, self.obj.feature)