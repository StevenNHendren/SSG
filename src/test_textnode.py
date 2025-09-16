import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN, "http:\\git.com")
        node2 = TextNode("This is a text node", TextType.PLAIN, "http:\\git.com")
        self.assertEqual(node, node2)
    def test_url_neq(self):
        node = TextNode("This is another text node", TextType.CODE, "http:\\git.com")
        node2 = TextNode("This is another text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_type_neq(self):
        node = TextNode("Some node or another", TextType.ITALIC)
        node2 = TextNode("Some node or another", TextType.PLAIN)
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()
