import re
from enum import Enum
from htmlnode import *

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def text_node_to_html_node(text_node):
    if text_node.text_type == None:
        raise Exception("text_type cannot be none")
    if not text_node.text_type in TextType:
        raise Exception("invalid TextType")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            n = node.text.count(delimiter)
            #print(f"Delimiter count: {n}")
            if n == 0:
                new_nodes.append(node)
            elif n == 2:
                split_list = []
                split_nodes = []
                split_list = node.text.split(delimiter)
                if len(split_list[0]) > 0:
                    split_nodes.append(TextNode(split_list[0], TextType.TEXT))
                if len(split_list[1]) > 0:
                    split_nodes.append(TextNode(split_list[1], text_type))
                if len(split_list[2]) > 0:
                    split_nodes.append(TextNode(split_list[2], TextType.TEXT))
                if len(split_nodes) > 0:
                    new_nodes.extend(split_nodes)
            elif n % 2 > 0:
                raise Exception("Closing delimiter not found")
            else:
                raise Exception("Node contains more than one inline element")
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches =  extract_markdown_images(node.text)
            if matches == None or len(matches) == 0:
                new_nodes.append(node)
            else:
                if len(matches) == 1:
                    image_alt, image_link = matches[0]
                    sections = node.text.split(f"![{image_alt}]({image_link})", 1)
                    if sections[0] != "":
                        new_nodes.append(TextNode(section[0], TextType.TEXT))
                    new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                    
                    

def split_nodes_link(old_nodes):
    pass

class TextType(Enum):
    TEXT = "text (plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
            #raise type error 
            #or return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
