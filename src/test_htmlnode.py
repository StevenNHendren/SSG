import unittest
from htmlnode import *

def test_none(self):
    node = HTMLNode(None, None, None, None)
    print(node)
    
def test_props_none(self):
    node = TextNode()
    print(node.props_to_html())
        
def test_props(self):
    node = TextNode("a", "Google", None, {"href": "https:\\www.google.com"})
    print(node.props_to_html())

def test_repr(self):
    node = TextNode("a", "Boot.Dev", None, {"href": "htts://bootdev.com"})
    print(node)

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_otherpara(self):
    node = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

def test_leaf_to_html_url(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
