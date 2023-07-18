from . import classes as c


class Fabric:
    def __init__(self, obj: c.Fish):
        self.obj_class = obj.__class__
        self.obj_attrs = obj.__dict__

    def do_copy(self):
        return self.obj_class(**self.obj_attrs)
