from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "text (plain)"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode()
    def __init__(self, text: str, text_type: TextType, url=None)
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other)
        if not isInstance(other, TextNode):
            return False
            #raise type error 
            #or return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def__repr__(self)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
