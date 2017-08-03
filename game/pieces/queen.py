from game.pieces.piece import Piece


class Queen(Piece):
	def canApplyAMovement(self, aMovement):
		return self._isADiagonalMovement(aMovement)
