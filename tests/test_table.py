from jusdat import Table, Column


def test_init_without_schema():
    table = Table('car')
    assert table.name == 'car'


def test_init_with_schema():
    table = Table('car', schema='vehicles')
    assert table.name == 'vehicles.car'


def test_column_handling():
    table = Table('car')
    column = table.color
    assert type(column) == Column
    assert column.name == 'color'


def test_column_handling_with_name_conflict():
    table = Table('car')
    name = table.name
    column = table.c.name

    assert type(name) != Column
    assert type(column) == Column
    assert column.name == 'name'
