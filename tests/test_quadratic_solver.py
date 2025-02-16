import unittest, sys
sys.path.append("src")
from quadratic_solver import solve_quadratic


class TestQuadraticSolver(unittest.TestCase):

    def test_two_real_roots(self):
        # Discriminant > 0
        result = solve_quadratic(1, -3, 2)
        self.assertAlmostEqual(result[0], 2.0)
        self.assertAlmostEqual(result[1], 1.0)

    def test_one_real_root(self):
        # Discriminant = 0
        result = solve_quadratic(1, 2, 1)
        self.assertAlmostEqual(result[0], -1.0)

    def test_complex_roots(self):
        # Discriminant < 0
        result = solve_quadratic(1, 1, 1)
        self.assertEqual(result[0].real, -0.5)
        self.assertAlmostEqual(result[0].imag, 0.86602540378)
        self.assertEqual(result[1].real, -0.5)
        self.assertAlmostEqual(result[1].imag, -0.86602540378)

    def test_invalid_coefficient_a(self):
        # a = 0 should raise ValueError
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)


if __name__ == "__main__":
    unittest.main()
