class Table:

    def __init__(self, name, schema=None):
        self.name = name
        if schema is not None:
            self.name = schema + '.' + self.name

