from game.pieces.piece import Piece


class Bishop(Piece):
	def canApplyAMovement(self, aMovement):
		return self._isADiagonalMovement(aMovement)
