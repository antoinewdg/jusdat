class Query:
    def __init__(self):
        self._parent = None

    def select(self, *args):
        return self._chain(CommaSeparatedQuery('SELECT', *args))

    def from_(self, *args):
        return self._chain(CommaSeparatedQuery('FROM', *args))

    def generate(self):
        return ''

    def and_(self, *args):
        return self._chain(SeparatedQuery(' AND ', None, *args))

    def or_(self, *args):
        return self._chain(SeparatedQuery(' OR ', None, *args))

    def _chain(self, query):
        query._parent = self
        return query

    def __str__(self):
        result = self.generate()
        if self._parent is not None:
            parent = str(self._parent)
            if parent != '':
                result = ' ' + result
            result = parent + result

        return result

    def __getattr__(self, name):
        return lambda *args: \
            self._chain(CommaSeparatedQuery(name.upper(), *args))


class SeparatedQuery(Query):
    def __init__(self, separator, prefix, *args):
        super().__init__()
        self.separator = separator
        self.prefix = prefix
        self._args = args

    def generate(self):
        result = ''
        if self.prefix is not None:
            result += self.prefix + ' '
        result += self.separator.join(str(arg) for arg in self._args)

        return result


class CommaSeparatedQuery(SeparatedQuery):
    def __init__(self, prefix, *args):
        super().__init__(', ', prefix, *args)


sql = Query()
