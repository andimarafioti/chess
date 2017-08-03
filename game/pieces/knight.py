from game.pieces.piece import Piece


class Knight(Piece):
	def canJumpAnotherPiece(self):
		return True

	def canApplyAMovement(self, aMovement):
		return not self._isADiagonalMovement(aMovement)