from enum import Enum, auto

class TokenType(Enum):
    HEADER = auto()
    Quote= auto()
    CODE_BLOCK = auto()
    TASK_MARKED = auto()
    TASK_UNMARKED = auto()
    UNORDERED_LIST = auto()     # should implement the nested elements
    ORDERED_LIST = auto()       # should implement the nested elements
    HORIZONTAL_RULE = auto()
    BOLD = auto()
    ITALIC = auto()
    LINK = auto()
    IMAGE = auto()
    STRIKETHROUGH = auto()
    HTML_COMMENT = auto()
    MD_COMMENT= auto()
    TABLE = auto()      # implement later
    ALERT = auto()      # implement later
    PARAGRAPH = auto()
    TEXT = auto()   
    EOF= auto()