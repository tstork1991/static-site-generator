import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_same_values(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Node 1 text", TextType.BOLD)
        node2 = TextNode("Node 2 text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://a.com")
        node2 = TextNode("Link text", TextType.LINK, "https://b.com")
        self.assertNotEqual(node1, node2)

    def test_equal_default_and_none_url(self):
        node1 = TextNode("Test", TextType.TEXT)
        node2 = TextNode("Test", TextType.TEXT, None)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
