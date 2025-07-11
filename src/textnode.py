from enum import Enum

class TextType(Enum):
    TEXT_PLAIN = "plaintext"
    TEXT_BOLD = "**bold**"
    TEXT_ITALIC = "*italic*"
    TEXT_CODE = "`code`"
    LINK_URL = "[link](url)"
    LINK_IMAGE = "![link](image)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        if self.text != value.text or self.text_type != value.text_type or self.url != value.url:
            return False
        return True
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'