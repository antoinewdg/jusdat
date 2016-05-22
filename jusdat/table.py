from .column import Column


class Table:
    def __init__(self, name, schema=None):
        self.c = self.ColumnsHandler(self)
        self._name = name
        if schema is not None:
            self._name = schema + '.' + self._name

    def __getattr__(self, name):
        return self.c.__getattr__(name)

    def __str__(self):
        return self._name

    class ColumnsHandler:

        def __init__(self, table):
            self.table = table
            self.columns = {}

        def __getattr__(self, name):
            if name not in self.columns:
                self.columns[name] = Column(name, self.table)
            return self.columns[name]
