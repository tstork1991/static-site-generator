import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_image_passes_non_text_node(self):
        node = TextNode("![image](https://a.com)", TextType.BOLD)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_link_passes_non_text_node(self):
        node = TextNode("[link](https://a.com)", TextType.ITALIC)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_no_images_returns_original(self):
        node = TextNode("Just some text", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_no_links_returns_original(self):
        node = TextNode("Just some text", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

if __name__ == "__main__":
    unittest.main()
