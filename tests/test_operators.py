from jusdat.operators import BinaryOperator, OperableMixin


class MockOperable(OperableMixin):
    def __str__(self):
        return 'a'


def test_binary_operator():
    operator = BinaryOperator('color', '=', 'red')
    assert str(operator) == 'color = red'


def test_equality_operator():
    a = MockOperable()
    operator = a == a
    assert str(operator) == 'a = a'


def test_inequality_operator():
    a = MockOperable()
    operator = a != a
    assert str(operator) == 'a != a'
