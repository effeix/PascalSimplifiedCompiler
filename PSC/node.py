class Node():
    def __init__(self, _value):
        self.value = _value
        self.children = []
    
    def set_child(self, child):
        self.children.append(child)