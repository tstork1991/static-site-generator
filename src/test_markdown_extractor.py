import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![one](http://a.com) and ![two](http://b.com)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("one", "http://a.com"),
            ("two", "http://b.com"),
        ], matches)

    def test_extract_markdown_links(self):
        text = "This is a [link](https://www.example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://www.example.com")], matches)

    def test_extract_multiple_links(self):
        text = "[first](http://a.com) then [second](http://b.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("first", "http://a.com"),
            ("second", "http://b.com"),
        ], matches)

    def test_image_not_matched_as_link(self):
        text = "Image: ![alt](http://img.png)"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_link_not_matched_as_image(self):
        text = "Link: [click](http://site.com)"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()
