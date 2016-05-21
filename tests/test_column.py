from jusdat import Column, Table


def test_conversion():
    table = Table('car')
    column = Column('color', table)
    assert str(column) == 'car.color'
