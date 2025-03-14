import unittest
from src.ATM import ATM, InvalidPinException


class ATMTestCase(unittest.TestCase):
    def test_raise_error_when_pin_is_wrong(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)

        with self.assertRaises(InvalidPinException):
            konto.check_balance(1235)

    def test_return_actual_balance(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)

        self.assertEqual(konto.check_balance(1234), 1000)

    def test_raise_error_when_pin_is_wrong_v2(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        with self.assertRaises(InvalidPinException):
            konto.deposit(1236, 1000)

    def test_succesful_deposit(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        konto.deposit(1234, 1000)
        self.assertEqual(konto.check_balance(1234), 2000)

    def test_raises_error_when_amount_is_lower_than_0(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        with self.assertRaises(ValueError):
            konto.deposit(1234, -10)

    def test_succesful_withdraw(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        konto.withdraw(1234, 500)
        self.assertEqual(konto.check_balance(1234), 500)

    def test_raise_error_when_amount_is_higher_than_balance(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        with self.assertRaises(ValueError):
            konto.withdraw(1234, 5000)

    def test_raises_error_when_pin_is_wrong_withdrawal(self):
        balance = 1000
        pin = 1234
        konto = ATM(balance, pin)
        with self.assertRaises(InvalidPinException):
            konto.withdraw(4321, 6000)


if __name__ == '__main__':
    unittest.main()