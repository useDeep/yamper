from ..common.pattern import BLOCK_PATTERNS
from ..common.token_type import TokenType
from .token import Token

class Lexer:
    def __init__(self, file_obj):
        self.file_obj= file_obj
        # self.lines= md.strip().split('\n')
        self.temp= (Token(TokenType.PARAGRAPH, ''))
        self.code_active= False
    
    def tokenize(self):
        for line in self.file_obj:
            line= line.rstrip('\n')
            if line.startswith('```') or self.code_active:
                if self.temp.value != '': yield self.temp
                # self.code_active= not self.code_active
                yield from self.handle_code_block(line)
            else:
                yield from self.next_block_token(line)
            #     if not self.code_active:
            #         self.temp= (Token(TokenType.PARAGRAPH, ''))
            #         continue
            # yield from self.next_block_token(line)
        if self.temp and self.temp.value:
            yield self.temp
        yield Token(type=TokenType.EOF, value='')

    def next_block_token(self, line):
        for pattern, token_type in BLOCK_PATTERNS.items():
            match = pattern.match(line)
            if match:
                if self.temp:
                    if token_type != TokenType.TEXT and (self.temp.type == TokenType.PARAGRAPH and self.temp.value == ''):
                        self.temp= (Token(token_type, match.group()))
                    elif token_type == TokenType.TEXT and self.temp.type != TokenType.HEADER and self.temp.type != TokenType.HORIZONTAL_RULE:
                        self.temp.value += '\n' + match.group()
                    else:
                        if self.temp.value != '': yield self.temp
                        self.temp= (Token(token_type, match.group()))
                else:
                    self.temp= (Token(token_type, match.group()))
                return

    def handle_code_block(self, line):
        if line.startswith('```'):
            if self.code_active:
                self.code_active = False
                yield self.code_block
                self.code_block = None
            else:
                if self.temp.value:
                    yield self.temp
                    self.temp = Token(TokenType.PARAGRAPH, '')
                self.code_active = True
                self.code_block = Token(TokenType.CODE_BLOCK, line + '\n')
        elif self.code_active:
            self.code_block.value += line + '\n'
        else:
            yield from self.next_block_token(line)

