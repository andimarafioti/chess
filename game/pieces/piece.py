class Piece(object):
	def __init__(self):
		super(Piece, self).__init__()

	def __repr__(self):
		return type(self).__name__

	def canJumpAnotherPiece(self):
		return False

	def canApplyAMovement(self, aMovement):
		raise NotImplementedError("Subclass Responsibility")

	def _isADiagonalMovement(self, aMovement):
		return abs(aMovement.initialRow() - aMovement.newRow()) == \
				abs(aMovement.initialColumn() - aMovement.newColumn())

	def _isAnStraightMovement(self, aMovement):
		return aMovement.initialRow() == aMovement.newRow() or aMovement.initialColumn() == aMovement.newColumn()
