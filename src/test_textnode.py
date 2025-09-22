import unittest

from textnode import *
#from textnode import TextNode, TextType


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
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")



if __name__ == "__main__":
    unittest.main()
