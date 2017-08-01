class Piece(object):
	def __init__(self):
		super(Piece, self).__init__()

	def canMoveFromTo(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		raise NotImplementedError("Subclass Responsibility")
