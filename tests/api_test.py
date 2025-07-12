import unittest
from src.api import get_crypto_price
from src.errors import APIError

class TestCryptoPriceAPI(unittest.TestCase):
    def test_get_crypto_price_valid(self):
        """Test fetching price for a valid cryptocurrency."""
        price = get_crypto_price('bitcoin')
        self.assertIn('inr', price)
        self.assertIn('usd', price)
        self.assertGreater(price['inr'], 0)
        self.assertGreater(price['usd'], 0)
        self.assertIsInstance(price['inr'], (int, float))
        self.assertIsInstance(price['usd'], (int, float))
        self.assertIsInstance(price, dict)
        
    def test_invalid_coin(self):
        with self.assertRaises(APIError):
            get_crypto_price("xyz123")

    def test_empty_string(self):
        with self.assertRaises(APIError):
            get_crypto_price("")

if __name__ == '__main__':
    unittest.main()