from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
