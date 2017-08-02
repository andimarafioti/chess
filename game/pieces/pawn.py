from game.pieces.piece import Piece


class Pawn(Piece):
	def canApplyAMovement(self, aMovement):
		return self._movementIsOneOrTwoStepsInAnyDirection(aMovement)

	def _movementIsOneOrTwoStepsInAnyDirection(self, aMovement):
		return aMovement.initialColumn() == aMovement.newColumn() and \
			0 < abs(aMovement.initialRow() - aMovement.newRow()) < 3
