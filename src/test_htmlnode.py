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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_otherpara(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_url(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.github.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.github.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_no_children(self):
        child_node = None
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_more_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("b", "grandchild 2")
        grandchild_node3 = LeafNode("b", "grandchild 3")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2, grandchild_node3])
        child_node2 = LeafNode("b", "child 2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b><b>grandchild 2</b><b>grandchild 3</b></span><b>child 2</b></div>")

                                 

