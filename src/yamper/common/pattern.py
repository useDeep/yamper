import re
from ..common.token_type import TokenType

BLOCK_PATTERNS= {
    re.compile(r'^(#{1,6})\s(.+)'): TokenType.HEADER,
    re.compile(r'^```'): TokenType.CODE_BLOCK,
    re.compile(r'^>\s*(.*)'): TokenType.Quote,
    re.compile(r'^- \[x\] (.+)$'): TokenType.TASK_MARKED,
    re.compile(r'^- \[ \] (.+)$'): TokenType.TASK_UNMARKED,
    re.compile(r'^[\-\+\*] (?!\[.\]).*'): TokenType.UNORDERED_LIST,
    re.compile(r'^\d+\. .*'): TokenType.ORDERED_LIST,
    re.compile(r'[ ]{0,3}(\-|\*|_){3,}[ ]*$'): TokenType.HORIZONTAL_RULE,
    re.compile(r'^\[.+]:\s+#\s*\(([\s\S]*?)\)\s*$'): TokenType.MD_COMMENT,
    re.compile(r'<!--.*'): TokenType.HTML_COMMENT,   # handle multiline comment (like code block)

    re.compile(r'^\s*$'): TokenType.PARAGRAPH,
    re.compile(r'^(?!\s*$).+'): TokenType.TEXT,
}

# INLINE_PATTERNS={
#     re.compile(r'\*\*(\S.*?)\*\*'): TokenType.BOLD,
#     re.compile(r'\_\_(\S.*?)\_\_'): TokenType.BOLD,
#     re.compile('\*(\S.*?)\*'): TokenType.ITALIC,
#     re.compile('\_(\S.*?)\_'): TokenType.ITALIC,
#     re.compile('`([^`\n]+)`'): TokenType.CODE_INLINE,
#     re.compile('\[(.*?)\]\((.*?)\)'): TokenType.LINK,
#     re.compile('\!\[(.*?)\]\((.*?)\)'): TokenType.LINK,
#     re.compile('~~(\s*[\s\S]*?\s*)~~'): TokenType.STRIKETHROUGH,
#     re.compile(':(\w+[-\w]*):'): TokenType.EMOJI,
#     re.compile('<!--\s*.*\s*-->'): TokenType.COMMENT,
# }



# Future Implementaions:
# Table
# Alerts/ admonations
# COLOR
# HTML  (Replace html comment token type to just html)
# MENTION
# FOOTNOTE
# SETEXT_HEADING
