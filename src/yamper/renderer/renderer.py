from .node import DocumentNode

class Renderer:
    def __init__(self):
        self.root = DocumentNode('div', '')

    def add_node(self, node):
        self.root.add_child(node)

    def to_html(self):
        return ''.join(self._generate_html(self.root))

    def _generate_html(self, node):
        if hasattr(node, 'is_self_closing'):
            if node.is_self_closing:
                yield f"<{node.tag}{node.attributes_string} />"
            else:
                yield f"<{node.tag}{node.attributes_string}>"
                yield node.value
                for child in node.children:
                    yield from self._generate_html(child)
                yield f"</{node.tag}>"
        else:
            yield f"{node}"