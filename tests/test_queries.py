from jusdat.queries import Query, CommaSeparatedQuery


def test_comma_separated_query():
    query = CommaSeparatedQuery('SELECT', 'color', 'engine')
    assert str(query) == 'SELECT color, engine'


def test_chaining():
    query = Query()
    query = query.select('color', 'engine')
    print(type(query._parent))
    assert str(query) == 'SELECT color, engine'


def test_chaining_on_custom_query():
    query = Query()
    query = query.strangename('color', 'engine')
    assert str(query) == 'STRANGENAME color, engine'


def test_multiple_chaining():
    query = Query()
    query = query.select('color').from_('car')
    assert str(query) == 'SELECT color FROM car'
