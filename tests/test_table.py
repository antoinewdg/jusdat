from jusdat.table import Table


def test_init_without_schema():
    table = Table('car')
    assert table.name == 'car'


def test_init_with_schema():
    table = Table('car', schema='vehicles')
    assert table.name == 'vehicles.car'
