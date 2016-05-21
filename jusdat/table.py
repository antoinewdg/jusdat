from .column import Column


class Table:
    def __init__(self, name, schema=None):
        self.c = self.ColumnsHandler()
        self.name = name
        if schema is not None:
            self.name = schema + '.' + self.name

    def __getattr__(self, name):
        return self.c.__getattr__(name)

    class ColumnsHandler:

        def __init__(self):
            self.columns = {}

        def __getattr__(self, name):
            if name not in self.columns:
                self.columns[name] = Column(name, self)
            return self.columns[name]
