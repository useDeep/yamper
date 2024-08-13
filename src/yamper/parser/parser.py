from .inline_processor import process_inline_text
from ..renderer.node import *
from ..renderer.renderer import Renderer
from ..lexer.token import Token
from ..common.token_type import TokenType
import re

class Parser:
    def __init__(self, lexer_generator):
        self.lexer_generator = lexer_generator
        self.cur_token = None
        self.renderer = Renderer()
        self.ul_block= []
        self.ol_block= []

    def parse(self):
        try:
            self.cur_token = next(self.lexer_generator)
            while self.cur_token.type != TokenType.EOF:
                if self.cur_token.type == TokenType.HEADER:
                    self.parse_header()
                elif self.cur_token.type == TokenType.PARAGRAPH or self.cur_token.type== TokenType.TEXT:
                    self.parse_paragraph()
                elif self.cur_token.type== TokenType.Quote:
                    self.parse_quote()
                elif self.cur_token.type == TokenType.HORIZONTAL_RULE:
                    self.parse_horizontal_rule()
                elif self.cur_token.type == TokenType.CODE_BLOCK:
                    self.parse_code_block()
                elif self.cur_token.type == TokenType.UNORDERED_LIST:
                    self.ul_block= []
                    while self.cur_token.type == TokenType.UNORDERED_LIST:
                        self.ul_block.append(self.cur_token)
                        self.cur_token = next(self.lexer_generator)
                    self.parse_unordered_list()
                    continue
                elif self.cur_token.type == TokenType.ORDERED_LIST:
                    self.ol_block= []
                    while self.cur_token.type == TokenType.ORDERED_LIST:
                        self.ol_block.append(self.cur_token)
                        self.cur_token = next(self.lexer_generator)
                    self.parse_ordered_list()
                    continue
                elif self.cur_token.type== TokenType.TASK_UNMARKED or self.cur_token.type == TokenType.TASK_MARKED:
                    self.parse_task()
                elif self.cur_token.type == TokenType.MD_COMMENT:
                    self.cur_token = next(self.lexer_generator)
                    continue
                elif self.cur_token.type== TokenType.HTML_COMMENT:
                    self.parse_HTML()
                else:
                    self.parse_HTML()

                # when support for more token types get added...
                self.cur_token = next(self.lexer_generator)
                if self.cur_token.type== TokenType.EOF:
                    break
        except StopIteration:
            print("Compilation interrupted")
        return self.renderer

    def parse_header(self):
        level = len(self.cur_token.value.split()[0])
        content = process_inline_text(' '.join(self.cur_token.value.split()[1:]))
        header_node = HeaderNode(content, level)
        self.renderer.add_node(header_node)

    def parse_paragraph(self):
        content = process_inline_text(self.cur_token.value)
        paragraph_node = ParagraphNode(content)
        self.renderer.add_node(paragraph_node)

    def parse_horizontal_rule(self):
        horizontal_rule_node = HorizonalRuleNode()
        self.renderer.add_node(horizontal_rule_node)

    def parse_code_block(self):
        lines= self.cur_token.value.split('\n')
        if lines[0].strip('`').split():
            language= lines[0].strip('```')
        else:
            language= None
        content= '\n'.join(lines[1:])
        code_block_node= CodeBlockNode(language, content)
        self.renderer.add_node(code_block_node)

    def parse_unordered_list(self):
        list_item_nodes= []
        for list_item in self.ul_block:
            content = process_inline_text(list_item.value.lstrip('- '))
            list_item_nodes.append(content)
        unordered_list_node= UnorderedListNode(list_item_nodes)
        self.renderer.add_node(unordered_list_node)
        self.ul_block= []
    
    def parse_ordered_list(self):
        list_item_nodes= []
        for list_item in self.ol_block:
            content = re.sub(r'^\d+\.\s*', '', list_item.value)
            content = process_inline_text(content)
            list_item_nodes.append(content)
        ordered_list_node= OrderedListNode(list_item_nodes)
        self.renderer.add_node(ordered_list_node)
        self.ol_block= []

    def parse_task(self):
        if self.cur_token.value.startswith('- [x]'):
            checked = True
            content = self.cur_token.value[5:].strip()
        elif self.cur_token.value.startswith('- [ ]'):
            checked = False
            content = self.cur_token.value[5:].strip()
        content= process_inline_text(content)
        task_node= TaskNode(content, checked)
        self.renderer.add_node(task_node)

    def parse_HTML(self):
        self.renderer.add_node(self.cur_token.value)

    def parse_quote(self):
        content = process_inline_text(self.cur_token.value.lstrip('>').strip())
        quote_node= QuoteNode(content)
        self.renderer.add_node(quote_node)