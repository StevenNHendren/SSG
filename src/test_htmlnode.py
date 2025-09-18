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

