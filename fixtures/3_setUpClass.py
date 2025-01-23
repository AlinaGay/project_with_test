import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """
        Возвращает сумму принятых аргументов,
        если аргументов нет, возвращает None.
        """
        if len(args) == 0:
            return None
        return sum(args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = TestCalc.calc.summ(1, 2, 3)
        self.assertEqual(act, 6, 'Wrong!')

    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act)

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(1)
        self.assertEqual(act, 1, 'Wrong!')


unittest.main()
