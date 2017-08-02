from game.pieces.piece import Piece


class Bishop(Piece):
	def canApplyAMovement(self, aMovement):
		return self._isADiagonalMovement(aMovement)

	def _isADiagonalMovement(self, aMovement):
		return abs(aMovement.initialRow() - aMovement.newRow()) == \
				abs(aMovement.initialColumn() - aMovement.newColumn())
