import unittest
from block_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines(self):
        md = """


Paragraph one


Paragraph two


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["Paragraph one", "Paragraph two"]
        )

    def test_leading_and_trailing_whitespace(self):
        md = "   \n\n  Hello  \n\n\n  World \n  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Hello", "World"])

if __name__ == "__main__":
    unittest.main()
