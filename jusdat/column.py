from .operators import OperableMixin


class Column(OperableMixin):
    def __init__(self, name, table):
        self.name = name
        self.table = table

    def __str__(self):
        return "%s.%s" % (self.table, self.name)
