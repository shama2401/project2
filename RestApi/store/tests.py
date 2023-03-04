def example(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2


from  django.test import TestCase


class OperationTestCase(TestCase):
    def test_plus(self):
        result = example(1,2,'+')
        self.assertEqual(3,result)
    def test_minus(self):
        result = example(1,2, '-')
        self.assertEqual(-1, result)
    def test_multiple(self):
        result = example(2, 2, '*')
        self.assertEqual(4, result)
    def test_devide(self):
        result = example(2, 2, '/')
        self.assertEqual(1, result)


