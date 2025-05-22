import unittest
from utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strip_spaces(self):
        self.assertEqual(extract_title("#   Welcome   "), "Welcome")

    def test_missing_title(self):
        with self.assertRaises(Exception):
            extract_title("## Subtitle only\nMore text")

if __name__ == "__main__":
    unittest.main()
