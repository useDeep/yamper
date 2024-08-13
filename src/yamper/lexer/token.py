class Token:
    def __init__(self, type, value):
        self.type= type
        self.value= value

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}')"