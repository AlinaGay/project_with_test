import unittest


class Calculator:
    """Производит арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_divider(self):
        act = TestCalc.calc.divider(2, 1)
        self.assertEqual(act, 2, 'текст, если проверка провалена')

    def test_divider_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.calc.divider, 1, 0)


unittest.main()
