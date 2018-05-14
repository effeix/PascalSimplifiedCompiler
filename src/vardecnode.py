from node import Node

class VarDecNode(Node):
	def eval(self, st):
		for child in self.children:
			child.eval(st)