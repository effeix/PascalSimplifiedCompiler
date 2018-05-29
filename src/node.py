from uuidmanager import UUIDManager


class Node():
    def __init__(self, _value=None):
        self.value = _value
        self.children = []
        self.identifier = UUIDManager.get_new()

    def set_child(self, child):
        self.children.append(child)