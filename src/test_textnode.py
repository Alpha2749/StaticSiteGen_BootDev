import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("Text node 1", TextType.PLAIN, "A")
        node2 = TextNode("a", TextType.URL)
        self.assertNotEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("Text node", TextType.PLAIN, "A")
        node2 = TextNode("Text node", TextType.PLAIN, "A")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()