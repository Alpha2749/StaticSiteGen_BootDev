import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", TextType.BOLD)
        print(node)


if __name__ == "__main__":
    unittest.main()