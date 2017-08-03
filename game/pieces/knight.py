from game.pieces.piece import Piece


class Knight(Piece):
	def canJumpAnotherPiece(self):
		return True

	def canApplyAMovement(self, aMovement):
		return not self._isADiagonalMovement(aMovement) and not self._isAnStraightMovement(aMovement) \
				and len(aMovement.path()) == 3
