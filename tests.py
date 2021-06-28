from unittest import TestCase
from quadratic_roots import equation_roots

NUMBER_RANDOM_CASES = 1000


def plus_numbers(a, b):
    return a + b


class QuadraticEquation(TestCase):
    def test_plus_numbers(self):
        # TODO: replace it or remove unused code
        first_number = 45
        second_number = 34
        required_result = 79
        function_result = plus_numbers(first_number, second_number)
        self.assertEqual(required_result, function_result)

    def test_determinant_zero(self):
        a, b, c = 1, 2, 1
        correct_roots = [-1, -1]
        x1, x2 = equation_roots(a, b, c)
        # TODO: replace to assertEqual
        self.assertTrue(correct_roots == [x1, x2])

    def test_determinant_negative(self):
        # TODO: test negative determinant
        # TODO: use assertIsNone
        self.assertTrue(True)

    def test_determinant_positive(self):
        # TODO: test positive determinant
        self.assertTrue(True)

    def test_random_parameters(self):
        for i in range(NUMBER_RANDOM_CASES):
            # TODO: generate random a, b, c
            # get roots
            # check quadratic equation equals zero
            # try to use
            pass
