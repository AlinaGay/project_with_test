# test_calculator.py
import unittest

from calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем MadCalculator."""

    def test_sum_string(self):
        """Тестирование функции sum_string с конкатенацией строк."""
        
        calc = MadCalculator()
        act = calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_negative_value(self):
        """Тестирование исключения с отрицательным числом."""
        calc = MadCalculator()
        with self.assertRaises(ValueError):
            calc.sum_string(1, -100500)

    def test_sum_args(self):
        """Тестирование функции суммирования аргументов."""
        # Создаём ещё один экземпляр класса MadCalculator.
        calc = MadCalculator()
        # Вызываем метод.
        act = calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')


unittest.main()
