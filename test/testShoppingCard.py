import unittest
from src.shopingCard import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.Cart = ShoppingCart()

    def test_add_product(self):
        print("** test_add_product()")
        result = self.Cart.add_product("Jablko", 5, 5)
        self.assertEqual(result, 1)

    def test_remove_product(self):
        print("** test_remove_product()")
        self.Cart.add_product("Jablko", 5, 5)
        result = self.Cart.remove_product("Jablko")
        self.assertEqual(result, 1)

    def test_update_quality(self):
        print("** test_update_quality()")
        result = self.Cart.update_quantity("Jablko", 3)
        self.assertEqual(result, 0)

    def test_get_products(self):
        print("** test_get_products()")
        self.Cart.add_product("gruszka", 5, 5)
        result = self.Cart.get_products()
        self.assertSequenceEqual(result, ["gruszka"])

    def test_count_products(self):
        print("** test_count_products()")
        self.Cart.add_product("jablko", 3, 5)
        self.Cart.add_product("gruszka", 6, 7)
        result = self.Cart.count_products()
        self.assertEqual(result, 12)

    def test_get_total_price(self):
        print("** test_get_total_price()")
        self.Cart.add_product("jablko", 3, 5)
        result = self.Cart.get_total_price()
        self.assertEqual(result, 15)

    def test_apply_discount_code(self):
        print("** test_apply_discount_code()")
        result = self.Cart.apply_discount_code("dsc10")
        self.assertEqual(result, 1)

    def test_checkout(self):
        print("** test_checkout()")
        result = self.Cart.checkout()
        self.assertEqual(result, 0)

    def tearDown(self):
        print("*** tearDown()")
        self.Cart = None
