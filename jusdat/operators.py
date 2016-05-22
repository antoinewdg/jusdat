from .parenthesis_rules import NeedsParenthesisMixin


class OperableMixin:
    def __eq__(self, other):
        return BinaryOperator(self, '=', other)

    def __ne__(self, other):
        return BinaryOperator(self, '!=', other)


class Operator(NeedsParenthesisMixin):
    pass


class BinaryOperator(Operator, OperableMixin):
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def __str__(self):
        return '%s %s %s' % (self.left, self.op, self.right)
