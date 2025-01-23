import unittest

from calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем MadCalculator."""

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        self.calc = MadCalculator()

    def test_sum_string(self):
        """Тестирование функции sum_string с конкатенацией строк."""
        act = self.calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_negative_value(self):
        """Тестирование исключения с отрицательным числом."""
        with self.assertRaises(ValueError):
            self.calc.sum_string(1, -100500)

    def test_sum_args(self):
        """Тестирование функции суммирования аргументов."""
        act = self.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')


unittest.main()
