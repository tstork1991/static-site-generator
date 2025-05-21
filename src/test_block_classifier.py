import unittest
from block_classifier import block_to_block_type
from block_type import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> quote\n> block"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item\n2. item\n3. item"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_invalid_ordered_list(self):
        # Skips a number — should fallback to paragraph
        self.assertEqual(block_to_block_type("1. one\n3. three"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
