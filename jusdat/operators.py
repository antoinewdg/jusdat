from .parenthesis_rules import NeedsParenthesisMixin


class OperableMixin:
    def __eq__(self, other):
        return BinaryOperator(self, '=', other)

    def __ne__(self, other):
        return BinaryOperator(self, '!=', other)

    def __add__(self, other):
        return BinaryOperator(self, '+', other)

    def __sub__(self, other):
        return BinaryOperator(self, '-', other)

    def __neg__(self):
        return UnaryOperator('-', self)


class Operator(NeedsParenthesisMixin):
    pass


class UnaryOperator(Operator, OperableMixin):
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __str__(self):
        return str(self.op) + str(self.value)


class BinaryOperator(Operator, OperableMixin):
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def __str__(self):
        return '%s %s %s' % (self.left, self.op, self.right)
