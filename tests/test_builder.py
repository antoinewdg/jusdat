from jusdat import sql


def test_builder():
    query = sql.select('color')
    assert str(query) == 'SELECT color'
