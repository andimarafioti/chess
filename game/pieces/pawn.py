from game.pieces.piece import Piece


class Pawn(Piece):
	def canApplyAMovement(self, aMovement):
		return aMovement.initialColumn() == aMovement.newColumn() and \
			self._movementIsOneOrTwoStepsInTheRightDirection(aMovement)

	def _movementIsOneOrTwoStepsInTheRightDirection(self, aMovement):
		if self.HAS_MOVED:
			return self._movementIsXStepsInTheRightDirection(aMovement, 1)
		else:
			return self._movementIsXStepsInTheRightDirection(aMovement, 2)

	def _movementIsXStepsInTheRightDirection(self, aMovement, x):
		if self._isWhite:
			condition = 0 < aMovement.newRow() - aMovement.initialRow() <= x
		else:
			condition = 0 < aMovement.initialRow() - aMovement.newRow() <= x
		return condition

	def canCaptureAnotherPieceWithAMovement(self, aMovement):
		return 0 < abs(aMovement.initialColumn() - aMovement.newColumn()) < 2 and \
			self._movementIsXStepsInTheRightDirection(aMovement, 1)
