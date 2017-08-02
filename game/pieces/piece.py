class Piece(object):
	def __init__(self):
		super(Piece, self).__init__()

	def canApplyAMovement(self, aMovement):
		raise NotImplementedError("Subclass Responsibility")
