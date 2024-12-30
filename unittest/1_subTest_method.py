from unittest import TestCase

from code import get_square


class TestExample(TestCase):

    def test_square(self):

        values_results = (
            (2, 4),
            (3, 10),
            (4, 20)
        )

        for value, expected_result in values_results:
            with self.subTest():
                result = get_square(value)
                self.assertEqual(result, expected_result)
