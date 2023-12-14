import unittest
from coin import Coin  

class TestMinCoinsCalculator(unittest.TestCase):
    def test_case_1(self):
        n = 1
        S = 1
        v = [1]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 1)

    def test_case_2(self):
        n = 2
        S = 5
        v = [1, 2]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 3)

    def test_case_3(self):
        n = 3
        S = 10
        v = [1, 3, 5]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 2)

    def test_case_4(self):
        n = 4
        S = 15
        v = [1, 2, 3, 4]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 4)

    def test_case_5(self):
        n = 5
        S = 20
        v = [2, 4, 5, 7, 9]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 3)

    def test_case_6(self):
        n = 6
        S = 25
        v = [2, 3, 5, 7, 11, 13]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 3)

    def test_case_7(self):
        n = 7
        S = 30
        v = [3, 7, 11, 13, 17, 19, 23]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 2)

    def test_case_8(self):
        n = 8
        S = 35
        v = [2, 5, 8, 10, 15, 20, 25, 30]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 2)

    def test_case_9(self):
        n = 9
        S = 40
        v = [3, 6, 9, 12, 15, 18, 21, 24, 27]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, -1)

    def test_case_10(self):
        n = 10
        S = 50
        v = [2, 5, 8, 10, 15, 20, 25, 30, 35, 40]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, 2)
        
    def test_no_solution(self):
        n = 3
        S = 7
        v = [2, 4, 6]

        calculator = Coin(n, S, v)
        result = calculator.calculate_min_coins()

        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
