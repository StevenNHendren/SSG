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
        node = TextNode("This is a text node", TextType.TEXT, "http:\\git.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "http:\\git.com")
        self.assertEqual(node, node2)
    def test_url_neq(self):
        node = TextNode("This is another text node", TextType.CODE, "http:\\git.com")
        node2 = TextNode("This is another text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_type_neq(self):
        node = TextNode("Some node or another", TextType.ITALIC)
        node2 = TextNode("Some node or another", TextType.TEXT)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
    def test_code(self):
        node = TextNode("This is a code text block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text block")
    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.microsoft.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props["href"], "https://www.microsoft.com")
    def test_image(self):
        node = TextNode("This is image alt text", TextType.IMAGE, "https://www.foodbanjo.com/wp-content/uploads/2024/04/air-fryer-pigs-in-a-blanket-7025-01.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "This is image alt text")
        self.assertEqual(html_node.props["src"], "https://www.foodbanjo.com/wp-content/uploads/2024/04/air-fryer-pigs-in-a-blanket-7025-01.jpg")



if __name__ == "__main__":
    unittest.main()
