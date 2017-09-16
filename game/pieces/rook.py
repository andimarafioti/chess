from game.pieces.piece import Piece


class Rook(Piece):
	def canApplyAMovement(self, aMovement):
		return self._isAnStraightMovement(aMovement)
