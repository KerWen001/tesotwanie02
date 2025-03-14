import unittest
from src.quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        #arrange
        a, b, c, = 0, 2, 4

        #act & assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_two_solutions(self):
        #arrange
        a, b, c, = 2,-8,6
        equation = QuadraticEquation(a,b,c)

        self.assertEqual(equation.solve(), (3,1))

    def test_one_solution(self):
        #arrange
        a, b, c, = 1,-6,9
        equation = QuadraticEquation(a,b,c)

        self.assertEqual(equation.solve(), (3,))

    def test_no_solutions(self):
        #arrange
        a, b, c, = 1,2,5
        equation = QuadraticEquation(a,b,c)

        self.assertEqual(equation.solve(), None)

if __name__ == '__main__':
    unittest.main()
