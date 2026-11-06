import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_fractional_weight_rounding(self):
        self.assertEqual(shipping_quote(1.234, "local"), 6.85)
        self.assertEqual(shipping_quote(1.234, "regional"), 9.85)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
