class Node:
    def __init__(self, tag='', value='', children= None, attributes=None, is_self_closing= False):
        self.tag = tag
        self.value = value 
        self.attributes = attributes or {}
        self.children = []
        self.is_self_closing = is_self_closing

    def add_child(self, child):
        self.children.append(child)

    @property
    def attributes_string(self):
        return ''.join(f' {k}="{v}"' for k, v in self.attributes.items())

class DocumentNode(Node):
    def __init__(self, tag, value):
        super().__init__(tag, value)

class HeaderNode(Node):
    def __init__(self, value, level):
        super().__init__(f'h{level}', value)

class ParagraphNode(Node):
    def __init__(self, value):
        super().__init__('p', value)

class HorizonalRuleNode(Node):
    def __init__(self):
        super().__init__('hr', is_self_closing=True)

class CodeBlockNode(Node):
    def __init__(self, language, value):
        super().__init__('pre')
        attributes= {'class': f"language-{language}"} if language else {}
        code_node= Node('code', value, attributes=attributes)
        self.add_child(code_node)

class UnorderedListNode(Node):
    def __init__(self, children):
        super().__init__('ul')
        for content in children:
            self.add_child(ListItemNode(content))

class OrderedListNode(Node):
    def __init__(self, children):
        super().__init__('ol')
        for content in children:
            self.add_child(ListItemNode(content))

class ListItemNode(Node):
    def __init__(self, value):
        super().__init__('li', value)

class TaskNode(Node):
    def __init__(self, value, checked):
        input_attributes = {'type': 'checkbox', 'disabled': 'true'}
        if checked:
            input_attributes['checked'] = 'checked'
        checkbox_node = Node('input', attributes=input_attributes, is_self_closing=True)
        label_node = Node('label', value)
        super().__init__('div')
        self.add_child(checkbox_node)
        self.add_child(label_node)

class QuoteNode(Node):
    def __init__(self, value):
        super().__init__('blockquote', value)