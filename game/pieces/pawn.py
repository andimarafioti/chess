from game.pieces.piece import Piece


class Pawn(Piece):
	def canApplyAMovement(self, aMovement):
		return aMovement.initialColumn() == aMovement.newColumn() and \
			self._movementIsOneOrTwoStepsInTheRightDirection(aMovement)

	def _movementIsOneOrTwoStepsInTheRightDirection(self, aMovement):
		if self._isWhite:
			condition = 0 < aMovement.newRow() - aMovement.initialRow() < 3
		else:
			condition = 0 < aMovement.initialRow() - aMovement.newRow() < 3
		return condition
