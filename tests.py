from unittest import TestCase
from quadratic_roots import equation_roots
import random

NUMBER_RANDOM_CASES = 100


class QuadraticEquation(TestCase):

    def test_determinant_zero(self):
        a, b, c = 1, 2, 1
        correct_roots = [-1, -1]
        x1, x2 = equation_roots(a, b, c)
        # TODO: replace to assertEqual
        self.assertEquals([x1, x2], correct_roots)

    def test_determinant_negative(self):
        # TODO: test negative determinant
        a, b, c, = 5, 8, 4
        x1, x2 = equation_roots(a, b, c)
        # TODO: use assertIsNone
        self.assertIsNone(x1, x2)
        pass

    def test_determinant_positive(self):
        # TODO: test positive determinant
        a, b, c = 2, 7, -4
        x1, x2 = equation_roots(a, b, c)
        correct_roots = [-4.0, 0.5]
        self.assertEquals([x1, x2], correct_roots)

    def test_random_parameters(self):
        for i in range(NUMBER_RANDOM_CASES):
            # TODO: generate random a, b, c
            a, b, c = random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)
            x1, x2 = equation_roots(a, b, c)
            if x1 is not None:
                equation_answer_1 = a * (x1 ** 2) + b * x1 + c
                equation_answer_2 = a * (x2 ** 2) + b * x2 + c
                self.assertAlmostEquals(equation_answer_1, equation_answer_2, 0)
