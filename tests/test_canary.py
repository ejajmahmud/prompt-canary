"""Unit tests for CanaryEngine."""
import unittest
from prompt_canary.canary import CanaryEngine

class TestCanaryEngine(unittest.TestCase):
    def test_encode_decode(self):
        secret = "CANARY-99"
        encoded = CanaryEngine.inject("Hello World", secret)
        self.assertTrue(CanaryEngine.has_canary(encoded, secret))
        decoded = CanaryEngine.decode_canary(encoded)
        self.assertEqual(decoded, secret)

    def test_clean_text_no_canary(self):
        self.assertFalse(CanaryEngine.has_canary("Normal clean text", "ANY"))

if __name__ == "__main__":
    unittest.main()
