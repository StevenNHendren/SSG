from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "text (plain)"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode()
    def __init__(self, text, text_type, url)
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self)
        
