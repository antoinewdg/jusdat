from jusdat.queries import Query, CommaSeparatedQuery, sql


def test_comma_separated_query():
    query = CommaSeparatedQuery('SELECT', 'color', 'engine')
    assert str(query) == 'SELECT color, engine'


def test_chaining():
    query = sql.select('color', 'engine')
    assert str(query) == 'SELECT color, engine'


def test_chaining_on_custom_query():
    query = sql.strangename('color', 'engine')
    assert str(query) == 'STRANGENAME color, engine'


def test_multiple_chaining():
    query = sql.select('color').from_('car')
    assert str(query) == 'SELECT color FROM car'


def test():
    from jusdat import Table
    car = Table('car')
    print(car._name)
    print(sql.select(car.color, car.s))


def test_and_query():
    query = sql.and_('a', 'b')
    assert str(query) == 'a AND b'


def test_or_query():
    query = sql.or_('a', 'b')
    assert str(query) == 'a OR b'

