import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode(None, None, None, None)
        print(node)
    
    def test_props_none(self):
        node = HTMLNode()
        print(node.props_to_html())
       
    def test_props(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com"})
        print(node.props_to_html())

    def test_repr(self):
        node = HTMLNode("a", "Boot.dot Dev", None, {"href": "https://bootdev.com"})
        print(node)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_otherpara(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_url(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.github.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.github.com">Click me!</a>')
