class Query:
    def __init__(self):
        self._parent = None

    def select(self, *args):
        return self._chain('SELECT', *args)

    def from_(self, *args):
        return self._chain('FROM', *args)

    def generate(self):
        return ''

    def _chain(self, query_prefix, *args):
        child = CommaSeparatedQuery(query_prefix, *args)
        child._parent = self
        return child

    def __str__(self):
        result = self.generate()
        if self._parent is not None:
            parent = str(self._parent)
            if parent != '':
                result = ' ' + result
            result = parent + result

        return result

    def __getattr__(self, name):
        return lambda *args: self._chain(name.upper(), *args)


class CommaSeparatedQuery(Query):
    def __init__(self, prefix, *args):
        super().__init__()
        self.prefix = prefix
        self._args = args

    def generate(self):
        result = self.prefix + ' ' + ', '.join((str(arg) for arg in self._args))
        return result


sql = Query()
