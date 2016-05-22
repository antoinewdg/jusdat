from jusdat.operators import BinaryOperator, UnaryOperator, OperableMixin


class MockOperable(OperableMixin):
    def __str__(self):
        return 'a'


def test_binary_operator():
    operator = BinaryOperator('color', '=', 'red')
    assert str(operator) == 'color = red'


def test_unary_operator():
    operator = UnaryOperator('-', 3)
    assert str(operator) == '-3'


def test_equality_operator():
    a = MockOperable()
    operator = a == a
    assert str(operator) == 'a = a'


def test_inequality_operator():
    a = MockOperable()
    operator = a != a
    assert str(operator) == 'a != a'


def test_addition_operator():
    a = MockOperable()
    operator = a + a
    assert str(operator) == 'a + a'
